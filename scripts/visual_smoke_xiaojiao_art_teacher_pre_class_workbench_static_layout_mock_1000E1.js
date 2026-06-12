const childProcess = require("child_process");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const OUT_DIR = path.join(ROOT, "docs\\audit\\screenshots\\xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1");
const SUMMARY = path.join(ROOT, "docs\\audit\\visual_smoke\\xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_summary.json");
const PAGES = [
  { id: "first_run_onboarding", file: "samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_1000E1.html" },
  { id: "initialized_workbench_home", file: "samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_1000E1.html" },
];
const VIEWPORTS = [
  { id: "desktop", width: 1440, height: 1100 },
  { id: "mobile", width: 390, height: 1100 },
];

function fileUrl(filePath) {
  return "file:///" + filePath.replace(/\\/g, "/");
}

function pngSize(buffer) {
  if (buffer.subarray(0, 8).toString("hex") !== "89504e470d0a1a0a") {
    throw new Error("not a PNG");
  }
  return { width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20) };
}

function main() {
  if (!fs.existsSync(CHROME)) {
    throw new Error("Chrome not found: " + CHROME);
  }
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.mkdirSync(path.dirname(SUMMARY), { recursive: true });
  const shots = [];
  for (const page of PAGES) {
    const html = path.join(ROOT, page.file);
    for (const viewport of VIEWPORTS) {
      const out = path.join(OUT_DIR, `${page.id}_${viewport.id}.png`);
      const args = [
        "--headless=new",
        "--disable-gpu",
        "--disable-extensions",
        "--disable-background-networking",
        "--disable-default-apps",
        "--no-first-run",
        `--window-size=${viewport.width},${viewport.height}`,
        `--screenshot=${out}`,
        fileUrl(html),
      ];
      const run = childProcess.spawnSync(CHROME, args, { encoding: "utf8" });
      if (run.status !== 0) {
        throw new Error(`Chrome screenshot failed for ${page.id} ${viewport.id}: ${run.stderr}`);
      }
      const buffer = fs.readFileSync(out);
      const size = pngSize(buffer);
      shots.push({
        page_id: page.id,
        viewport: viewport.id,
        path: path.relative(ROOT, out).replace(/\\/g, "/"),
        width: size.width,
        height: size.height,
        bytes: buffer.length,
      });
    }
  }
  fs.writeFileSync(SUMMARY, JSON.stringify({
    stage_code: "1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK",
    visual_smoke_completed: true,
    real_frontend_modified: false,
    runtime_connected: false,
    screenshots: shots,
  }, null, 2));
  console.log("ALL_1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_CHECKS_OK_SCREENSHOTS_OK");
}

main();

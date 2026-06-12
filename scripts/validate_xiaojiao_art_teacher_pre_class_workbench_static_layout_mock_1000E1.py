from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

STAGE_CODE = '1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK'
FINAL_STATUS = 'XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_PASS'
SLUG = 'xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1'
MARKER = 'ALL_1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_CHECKS_OK'
NEXT_STAGE = '1000E2_WORK_STATE_TO_DYNAMIC_PANEL_RENDERING_PENDING_REVIEW'
REQUIRED_FILES = ['docs/foundation/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.json', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0_result.json', 'docs/foundation/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.md', 'docs/foundation/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.json', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_report.md', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_result.json', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_checklist.json', 'docs/audit_packages/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_manifest.json', 'scripts/validate_xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.py', 'scripts/visual_smoke_xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.js', 'samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/sample_index_1000E1.json', 'samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/layout_contract_1000E1.json', 'samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/xiaojiao_static_layout_1000E1.css', 'samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_1000E1.html', 'samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_1000E1.html', 'docs/audit/visual_smoke/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_summary.json', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_desktop.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_mobile.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_desktop.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_mobile.png', 'docs/audit_packages/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.zip']
BOUNDARY_FALSE_KEYS = ['database_written', 'memory_written', 'feishu_written', 'formal_export_created', 'classroom_student_runtime_connected', 'provider_called', 'frontend_runtime_modified', 'backend_runtime_modified', 'old_sealed_stage_modified', 'full_repo_blind_rename_performed', 'teacher_facing_jarvis_wording_introduced', 'teacher_facing_xiaobei_wording_introduced', 'entered_1000E2', 'entered_1000F']
SCREENSHOTS = ['docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_desktop.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_mobile.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_desktop.png', 'docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_mobile.png']


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def png_size(path: Path):
    data = path.read_bytes()
    if data[:8].hex() != "89504e470d0a1a0a":
        fail(f"not png: {path}")
    return data[16:20], data[20:24], len(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(f"missing required file: {rel}")

    contract = load_json(root / f"docs/foundation/{SLUG}.json")
    result = load_json(root / f"docs/audit/{SLUG}_result.json")
    manifest = load_json(root / f"docs/audit_packages/{SLUG}_manifest.json")
    visual = load_json(root / "docs/audit/visual_smoke/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1_summary.json")
    html_text = "\n".join((root / rel).read_text(encoding="utf-8") for rel in [
        f"samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_1000E1.html",
        f"samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_1000E1.html",
        f"samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/xiaojiao_static_layout_1000E1.css",
    ])

    if contract.get("stage_code") != STAGE_CODE or contract.get("stage_type") != "static_layout_mock_only":
        fail("contract identity mismatch")
    if result.get("final_status") != FINAL_STATUS or result.get("pass") is not True:
        fail("result mismatch")
    if result.get("marker") != MARKER:
        fail("marker mismatch")
    if contract.get("next_stage") != NEXT_STAGE or result.get("next_stage") != NEXT_STAGE:
        fail("next stage mismatch")
    for key in BOUNDARY_FALSE_KEYS:
        if result.get("boundary_flags", {}).get(key) is not False:
            fail(f"unsafe boundary flag: {key}")

    gates = contract.get("sufficiency_gates", {})
    for key in ["initialization_sufficiency_gate", "artifact_draft_sufficiency_gate", "precision_generation_gate"]:
        if key not in gates:
            fail(f"missing gate: {key}")
    if "可先生成草稿，教材目录/校历待复核" not in json.dumps(contract, ensure_ascii=False) + html_text:
        fail("draft allowed with review gaps message missing")
    for term in [
        "first_run_onboarding",
        "initialized_workbench_home",
        "小教引导式工作台初始化",
        "Initialization Sufficiency Gate",
        "blocking_required",
        "recommended_required",
        "precision_required",
        "小教按步骤帮你建立本学期工作空间",
        "不替代学期周历表",
    ]:
        if term not in json.dumps(contract, ensure_ascii=False) + html_text:
            fail(f"missing required term: {term}")

    if visual.get("visual_smoke_completed") is not True:
        fail("visual smoke not completed")
    if visual.get("real_frontend_modified") is not False or visual.get("runtime_connected") is not False:
        fail("visual smoke boundary flags unsafe")
    if len(visual.get("screenshots", [])) != 4:
        fail("expected four screenshots")
    for rel in SCREENSHOTS:
        _, _, byte_len = png_size(root / rel)
        if byte_len < 5000:
            fail(f"screenshot too small: {rel}")

    with zipfile.ZipFile(root / f"docs/audit_packages/{SLUG}.zip", "r") as zf:
        zip_entries = zf.namelist()
    for entry in zip_entries:
        normalized = entry.replace("\\", "/")
        if normalized.startswith("/") or ":" in normalized:
            fail(f"unsafe zip path: {entry}")
        if any(part in normalized.lower() for part in [".env", "token", "secret", "node_modules", "__pycache__", ".db", ".sqlite"]):
            fail(f"forbidden zip entry: {entry}")
    if manifest.get("manifest_minus_zip") != [] or manifest.get("zip_minus_manifest") != []:
        fail("manifest alignment fields not empty")
    if sorted(manifest.get("zip_entries", [])) != sorted(zip_entries):
        fail("manifest entries mismatch zip")
    print(MARKER)
    return 0


if __name__ == "__main__":
    sys.exit(main())

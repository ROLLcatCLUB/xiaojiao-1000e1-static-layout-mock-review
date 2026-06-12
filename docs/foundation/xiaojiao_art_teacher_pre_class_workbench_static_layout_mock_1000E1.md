# 1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK

Date: 2026-06-12

## Stage Identity

```text
stage_code=1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK
stage_name=Art Teacher Pre-Class Workbench Static Layout Mock
stage_type=static_layout_mock_only
final_status_target=XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_PASS
next_stage=1000E2_WORK_STATE_TO_DYNAMIC_PANEL_RENDERING_PENDING_REVIEW
```

## Purpose

1000E1 is the first product-shape mock stage. It creates a static, reviewable layout for the art teacher pre-class workbench without modifying real frontend pages or connecting runtime.

## Required Product States

1. `first_run_onboarding / 工作台初始化态`
2. `initialized_workbench_home / 已初始化教师动态工作台首页`

## Sufficiency Gate Correction

1000E1 absorbs the E0 review caveat:

- Initialization Sufficiency Gate: missing `role_profile`, `subject`, `semester`, or `grade_or_class_scope` prevents the full workbench from unfolding.
- Artifact Draft Sufficiency Gate: once basic initialization is done, the teaching work plan can show `可先生成草稿，教材目录/校历待复核`.
- Precision Generation Gate: textbook catalog, school calendar, unit sequence, and lesson topics affect precise calendar and lesson allocation, not the initial draft.

## Static Layout Pages

- `samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_1000E1.html`
- `samples/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_1000E1.html`

## Screenshot Evidence

- `docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_desktop.png`
- `docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/first_run_onboarding_mobile.png`
- `docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_desktop.png`
- `docs/audit/screenshots/xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1/initialized_workbench_home_mobile.png`

## Boundaries

This stage does not implement real UI, modify real frontend pages, connect runtime, call provider/model, write database, write memory, write Feishu, create formal export, connect classroom student runtime, perform blind rename, enter 1000E2, or enter 1000F.

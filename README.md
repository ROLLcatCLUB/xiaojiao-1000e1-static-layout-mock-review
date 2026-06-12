# Xiaojiao 1000E1 Static Layout Mock Review

This repository is a dedicated GitHub review area for:

1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK

It is not the full xiaobei-core source repository.

## Stage

| Stage | final_status | Validator marker |
| --- | --- | --- |
| 1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK | XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_PASS | ALL_1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_CHECKS_OK |

## Validator commands

`powershell
python scripts/validate_xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.py
python scripts/validate_xiaojiao_art_teacher_pre_class_workbench_static_layout_mock_1000E1.py --root .
`

## Review focus

请审核 1000E1 是否可以作为 1000E2 前的静态布局 mock：

- 是否包含 first-run onboarding / 工作台初始化态
- 是否包含 initialized workbench home / 已初始化教师动态工作台首页
- 首次进入是否友好，不是空白聊天，也不是一堆空面板
- 小教是否像引导者，而不是死表单
- 三道门是否表达清楚：Initialization Sufficiency Gate / Artifact Draft Sufficiency Gate / Precision Generation Gate
- 教学工作计划面板是否表达“基础信息完成后可先生成草稿，教材目录/校历待复核”
- 主工作区是否优先，小教建议是否轻量，工作记录抽屉是否次要
- Dynamic panels 是否不像固定死卡片
- 周工作图谱是否没有替代学期周历表
- 是否继续守住硬边界：不写真实 UI、不改真实 frontend、不接 runtime/provider/model/database/memory/Feishu/formal export/课堂学生端、不 blind rename
- 是否可以进入 1000E2_WORK_STATE_TO_DYNAMIC_PANEL_RENDERING_PENDING_REVIEW

注意：这里是 review area，不是完整源码仓库。1000E1 是静态布局 mock，不是 UI/runtime apply。
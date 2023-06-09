from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class QuestStageOption:
    id: str
    quest_stage: "QuestStage"  # Reference to the parent quest stage

    text: str
    next_stage_id: str
    response_message: Optional[str] = None


@dataclass
class QuestStage:
    id: str
    quest: "Quest"  # Reference to the parent quest

    location_id: str
    text: str
    options: Dict[str, QuestStageOption] = field(default_factory=dict)

    def __post_init__(self):
        updated_options = {}
        for option_id, option in self.options.items():
            if (isinstance(option, dict)):
                updated_options[option_id] = QuestStageOption(
                    id=option_id,
                    quest_stage=self,
                    **option)
        self.options = updated_options


@dataclass
class Quest:
    id: str

    name: str
    description: str
    start_stage_id: str
    stages: Dict[str, QuestStage] = field(default_factory=dict)

    def __post_init__(self):
        updated_stages = {}
        for stage_id, stage in self.stages.items():
            if (isinstance(stage, dict)):
                updated_stages[stage_id] = QuestStage(
                    id=stage_id,
                    quest=self,
                    **stage)
        self.stages = updated_stages

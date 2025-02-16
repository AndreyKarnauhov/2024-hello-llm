"""
Starter for demonstration of laboratory work.
"""
# pylint: disable= too-many-locals, undefined-variable, unused-import
from pathlib import Path

from core_utils.llm.time_decorator import report_time
from main import RawDataImporter, RawDataPreprocessor
from config.lab_settings import LabSettings
from config.constants import PROJECT_ROOT


@report_time
def main() -> None:
    """
    Run the translation pipeline.
    """
    settings = LabSettings(PROJECT_ROOT/'lab_7_llm'/'settings.json')
    importer = RawDataImporter(settings.parameters.dataset)
    importer.obtain()

    preprocessor = RawDataPreprocessor(importer.raw_data)
    print(preprocessor.analyze())

    result = None
    assert result is not None, "Demo does not work correctly"


if __name__ == "__main__":
    main()

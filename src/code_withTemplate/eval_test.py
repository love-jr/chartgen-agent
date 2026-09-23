import os
import sys

from eval_chart import eval_chart

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from config.list import chart_themes,chart_types,color_matchings,topics,Single_broken_line,multiple_broken_lines,Single_broken_line_dotted,multiple_broken_lines_dotted,Single_Pie_Chart,simple_bar_chart,paired_bar_chart,simple_column_chart,paired_column_chart
from src.utils.api_config import APIConfig
from src.utils.api_config_doubao import APIConfig_DouBao

from src.utils.api_client import APIClient

def main():
    """主程序"""
    config = APIConfig_DouBao()
    client = APIClient(config)
    re= eval_chart(client, "/data/yangyuming/projects/chart_generation/chartWithTemplate/chart_0001/chart.png")
    print(re)

if __name__ == "__main__":
    main()
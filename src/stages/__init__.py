"""三阶段框架的公共阶段实现。

论文框架把「从主题到成图」拆成三个阶段：

1. **数据生成** —— ``data.generate_data``
2. **代码生成** —— 两条路线各自实现（提示词不同），见
   ``code_withTemplate/code_generator.py``、``code_withoutTemplate/code_generator.py``
3. **评估与优化** —— ``execute.run_r_code`` 出图 + ``evaluate.eval_chart`` 打分

原先阶段 ①③ 在 ``code_withTemplate/``、``code_withoutTemplate/``、
``code_optimazation/`` 下各复制了一份，差异仅在输出目录前缀。此处收敛。
"""

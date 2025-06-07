# 智能体核心组件
class KnowledgeAgent:
    def __init__(self):
        self.tools = {
            'rag_tool': AdvancedRAGTool(),
            'sql_tool': SQLQueryTool(),
            'web_tool': WebSearchTool()
        }
        self.memory = ConversationMemory()
        self.planner = QueryPlanner()
        self.reflector = SelfReflection()
    
    def process_complex_query(self, query):
        # 1. 查询规划
        plan = self.planner.create_plan(query)
        
        # 2. 工具调用
        results = []
        for step in plan.steps:
            tool_result = self.execute_tool(step)
            results.append(tool_result)
        
        # 3. 结果整合
        final_answer = self.synthesize_results(results)
        
        # 4. 自我反思
        refined_answer = self.reflector.improve(final_answer)
        
        return refined_answer
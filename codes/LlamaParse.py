# LlamaParse工作流程示例
class DocumentProcessor:
    def __init__(self):
        self.parser = LlamaParse()
    
    def parse_complex_document(self, pdf_path):
        # 1. 文档结构分析
        structure = self.parser.analyze_structure(pdf_path)
        
        # 2. 多模态元素提取
        text_chunks = structure.extract_text_chunks()
        tables = structure.extract_tables()
        images = structure.extract_images()
        
        # 3. 语义关联建立
        linked_content = self.create_semantic_links(
            text_chunks, tables, images
        )
        
        return linked_content
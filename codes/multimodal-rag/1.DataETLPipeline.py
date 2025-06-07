class DataETLPipeline:
    def __init__(self):
        self.extractors = {
            'pdf': PDFExtractor(),
            'excel': ExcelExtractor(),
            'ppt': PPTExtractor(),
            'image': OCRExtractor()
        }
        self.transformer = DataTransformer()
        self.loader = IndexLoader()
    
    def process(self, file_path):
        # Extract 提取
        file_type = self.detect_file_type(file_path)
        raw_content = self.extractors[file_type].extract(file_path)
        
        # Transform 转换
        structured_content = self.transformer.transform(raw_content)
        
        # Load 加载
        self.loader.load_to_index(structured_content)
        
        return structured_content

# ETL (Extract-Transform-Load) 就像一个数据搬运和加工的流水线，它将散乱在各处的原始数据，加工成规整、干净、可用的数据，并最终存放到一个中央仓库里。

# 1.  **提取 (Extract)**：从各种不同的源头（如数据库、应用程序、文件等）获取原始数据。
# 2.  **转换 (Transform)**：将提取出的数据进行清洗、整合、转换，使其符合目标系统的标准和格式。这个过程可能包括：
#     *   **清洗**：处理缺失值、修正错误、去除重复数据。
#     *   **整合**：将来自不同源头的数据合并在一起。
#     *   **转换**：改变数据格式或结构，例如，将日期格式统一或进行计算。
# 3.  **加载 (Load)**：将转换后的高质量数据加载到目标数据库或数据仓库中，以供后续的分析和使用。




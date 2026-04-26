# Emotional Support AI — Demo Project

说明
- 这是一个最小可运行的情感支持（演示）项目，后端使用 FastAPI，通过 OpenAI Chat API 生成回复。
- 仅用于学习/演示，不建议直接对外提供临床/正式咨询服务。

快速开始
1. 复制仓库到本地：
   ```bash
   git clone <your-repo-url>
   cd <repo-dir>
   ```

2. 建立并激活虚拟环境（推荐）：
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\Scripts\activate       # Windows
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 配置环境变量（复制 .env.example -> .env 并填入你的 OpenAI Key）：
   ```bash
   cp .env.example .env
   # 编辑 .env 填入 OPENAI_API_KEY
   export OPENAI_API_KEY="sk-..."   # 或在 .env 中设置并使用 dotenv 管理
   ```

5. 运行本地服务：
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   然后打开 http://localhost:8000/static/index.html

重要安全与合规建议
- 明确声明这是非临床工具，不替代专业心理咨询或医疗。
- 加入危机识别逻辑：当用户提到自伤、自杀或伤害他人时，应立即在回复中提供当地危机热线并建议寻求紧急帮助；并在后端记录并触发人工干预流程（如果你有运营团队）。
- 隐私与数据最小化：尽量不要存储敏感对话；若必须存储要加密、获得用户同意并遵守相关法律（例如 GDPR）。
- 审计与可控性：限制模型输出风险（使用 system prompt、回复模版、敏感词检测等）。
- 日志与监控：记录并定期抽检对话以优化安全策略。

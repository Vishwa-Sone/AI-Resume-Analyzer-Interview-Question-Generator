skills_db = [
        # programming languages
        "python", "javascript", "typescript", "java", "c", "c++", "c#", "go", "rust", "swift",
        "kotlin", "r", "ruby", "php", "scala", "perl", "matlab", "bash", "shell scripting",
        "powershell", "dart", "lua", "haskell", "elixir", "groovy", "julia", "solidity", "assembly",

        # web frontend
        "html", "css", "react", "angular", "vue.js", "next.js", "nuxt.js", "svelte", "jquery",
        "bootstrap", "tailwind css", "sass/scss", "webpack", "vite", "responsive design",
        "accessibility", "progressive web apps", "redux", "zustand",

        # web backend
        "node.js", "express.js", "django", "flask", "fastapi","fast api", "spring boot", "laravel",
        "ruby on rails", "asp.net", "gin", "echo", "fiber", "nestjs", "grpc", "microservices",
        "rest apis", "graphql", "websockets", "authentication", "oauth", "jwt",

        # data science & analytics
        "pandas", "numpy", "matplotlib", "seaborn", "plotly", "tableau", "power bi", "excel",
        "google analytics", "statistics", "data visualization", "a/b testing", "data cleaning",
        "feature engineering", "jupyter", "spss", "sas", "looker", "metabase", "dax",
        "data storytelling", "hypothesis testing", "regression analysis",

        # machine learning & ai
        "machine learning", "deep learning", "tensorflow", "pytorch", "keras", "scikit-learn",
        "xgboost", "lightgbm", "nlp", "computer vision", "reinforcement learning", "transformers",
        "hugging face", "opencv", "mlops", "model deployment", "llms", "prompt engineering",
        "langchain", "rag", "stable diffusion", "onnx", "cuda","data structures","algorithms",
        "system design","unit testing","api design","model evaluation",

        # devops & cloud
        "docker", "kubernetes", "terraform", "ansible", "jenkins", "github actions", "gitlab ci",
        "circleci", "aws", "azure", "google cloud platform", "heroku", "vercel", "netlify",
        "ci/cd", "linux", "nginx", "apache", "monitoring", "grafana", "prometheus",
        "elk stack", "datadog", "new relic", "on-call practices", "incident management",

        # databases
        "sql", "mysql", "postgresql", "sqlite", "oracle", "microsoft sql server", "mongodb",
        "redis", "cassandra", "dynamodb", "firebase", "elasticsearch", "neo4j", "influxdb",
        "snowflake", "bigquery", "redshift", "data warehousing", "etl", "data modeling",
        "database design", "performance tuning", "replication", "backup and recovery",

        # security
        "networking", "firewalls", "encryption", "vulnerability assessment", "penetration testing",
        "siem tools", "threat analysis", "authorization", "ssl/tls", "pki", "zero trust",
        "owasp", "incident response", "compliance", "risk assessment", "ethical hacking",
        "burp suite", "wireshark", "nmap", "metasploit",

        # tools & platforms
        "git", "github", "gitlab", "bitbucket", "jira", "confluence", "notion", "slack",
        "postman", "swagger", "vs code", "intellij idea", "eclipse", "xcode", "android studio",
        "figma", "adobe xd", "photoshop", "illustrator", "unity", "unreal engine",
        "selenium", "cypress", "playwright", "jest", "pytest", "junit", "npm", "pip",

        # soft skills
        "communication", "leadership", "teamwork", "problem solving", "critical thinking",
        "time management", "adaptability", "creativity", "collaboration", "conflict resolution",
        "presentation", "mentoring", "decision making", "analytical thinking", "attention to detail",
        "customer service", "negotiation", "empathy", "active listening", "documentation",

        # project & product management
        "agile", "scrum", "kanban", "waterfall", "roadmapping", "stakeholder management",
        "prioritization", "sprint planning", "retrospectives", "user research", "requirements gathering",
        "risk management", "okrs", "kpis", "backlog grooming", "product strategy",
        "release management", "change management", "prince2", "pmp", "safe", "facilitation",

        # embedded & hardware
        "microcontrollers", "rtos", "firmware development", "arduino", "raspberry pi",
        "communication protocols", "i2c", "spi", "uart", "can bus", "fpga", "verilog", "vhdl",
        "pcb design", "sensors", "actuators", "debugging", "oscilloscope", "logic analyzer",

        # mobile development
        "swiftui", "jetpack compose", "react native", "flutter", "ionic", "xamarin",
        "push notifications", "app store deployment", "play store deployment",
        "mobile ui/ux", "in-app purchases", "sqlite", "realm",
    ]

job_roles_skills = {
    "software engineer": [
        "python", "data structures", "algorithms", "git", "sql", "rest apis", "fastapi",
        "system design", "unit testing", "linux", "ci/cd",
        "oop", "design patterns", "debugging", "api design"
    ],
    "data scientist": [
        "python", "machine learning", "statistics", "sql", "data visualization",
        "pandas", "numpy", "feature engineering", "jupyter", "communication",
        "scikit-learn", "model evaluation", "data cleaning", "big data tools"
    ],
    "machine learning engineer": [
        "python", "machine learning", "deep learning", "tensorflow", "pytorch",
        "mlops", "data pipelines", "sql", "git", "system design",
        "model deployment", "docker", "feature stores", "monitoring"
    ],
    "frontend developer": [
        "html", "css", "javascript", "react", "typescript", "rest apis",
        "git", "responsive design", "accessibility", "unit testing",
        "state management", "browser dev tools", "performance optimization"
    ],
    "backend developer": [
        "python", "node.js", "sql", "rest apis", "system design", "fastapi",
        "docker", "git", "linux", "authentication", "databases",
        "api security", "caching", "message queues"
    ],
    "devops engineer": [
        "linux", "docker", "kubernetes", "ci/cd", "terraform",
        "bash scripting", "git", "cloud platforms", "monitoring", "networking",
        "logging", "security best practices", "sre principles"
    ],
    "data engineer": [
        "python", "sql", "data pipelines", "apache spark", "airflow",
        "cloud platforms", "etl", "git", "linux", "databases",
        "data warehousing", "stream processing", "data modeling"
    ],
    "product manager": [
        "communication", "roadmapping", "stakeholder management", "agile",
        "data analysis", "user research", "sql", "prioritization",
        "documentation", "leadership",
        "metrics", "product analytics tools"
    ],
    "ux designer": [
        "figma", "user research", "wireframing", "prototyping", "accessibility",
        "communication", "visual design", "responsive design", "css", "collaboration",
        "usability testing", "interaction design"
    ],
    "cybersecurity analyst": [
        "networking", "linux", "python", "threat analysis", "encryption",
        "siem tools", "vulnerability assessment", "authentication",
        "firewalls", "communication",
        "incident response", "penetration testing", "security frameworks"
    ],
    "cloud architect": [
        "cloud platforms", "system design", "networking", "docker", "kubernetes",
        "terraform", "security", "linux", "ci/cd", "cost optimization",
        "multi-cloud strategy", "high availability design", "disaster recovery"
    ],
    "database administrator": [
        "sql", "databases", "performance tuning", "backup and recovery",
        "linux", "replication", "monitoring", "security", "python", "documentation",
        "query optimization", "indexing strategies"
    ],
    "qa engineer": [
        "unit testing", "automation testing", "python", "rest apis",
        "git", "bug tracking", "selenium", "communication", "agile", "documentation",
        "test case design", "performance testing", "api testing"
    ],
    "business analyst": [
        "sql", "data analysis", "communication", "documentation",
        "stakeholder management", "excel", "data visualization",
        "requirements gathering", "agile", "presentation",
        "business process modeling", "domain knowledge"
    ],
    "mobile developer": [
        "swift", "kotlin", "react native", "rest apis", "git",
        "unit testing", "ui/ux fundamentals", "firebase",
        "typescript", "accessibility",
        "app performance optimization", "state management"
    ],
    "full stack developer": [
        "javascript", "react", "node.js", "sql", "rest apis",
        "docker", "git", "html", "css", "authentication",
        "system design", "state management", "testing"
    ],
    "site reliability engineer": [
        "linux", "python", "kubernetes", "monitoring", "ci/cd",
        "incident management", "bash scripting", "networking",
        "docker", "on-call practices",
        "sla/slo/sli", "distributed systems"
    ],
    "embedded systems engineer": [
        "c", "c++", "rtos", "microcontrollers", "debugging", "linux",
        "firmware development", "communication protocols", "git",
        "low-level programming"
    ],
    "blockchain developer": [
        "solidity", "ethereum", "smart contracts", "python", "javascript",
        "cryptography", "web3.js", "git", "rest apis", "system design"
    ],
    "ar/vr developer": [
        "unity", "c#", "3d modeling", "opengl", "c++", "python",
        "git", "spatial computing", "ui/ux fundamentals", "performance optimization"
    ],
    "game developer": [
        "unity", "c#", "c++", "game physics", "3d modeling", "git",
        "performance optimization", "debugging", "ui/ux fundamentals", "scripting"
    ],
    "robotics engineer": [
        "python", "c++", "ros", "computer vision", "machine learning",
        "kinematics", "sensors", "linux", "debugging", "simulation",
        "control systems", "path planning"
    ],
    "data analyst": [
        "sql", "python", "excel", "data visualization", "statistics",
        "tableau", "communication", "data cleaning", "reporting", "critical thinking",
        "dashboarding", "business understanding"
    ],
    "bi developer": [
        "sql", "power bi", "tableau", "data warehousing", "etl",
        "data modeling", "excel", "dax", "python", "communication",
        "data governance", "dashboard performance tuning"
    ],
    "network engineer": [
        "networking", "cisco", "firewalls", "routing & switching", "linux",
        "vpn", "monitoring", "tcp/ip", "security", "troubleshooting",
        "network security", "cloud networking"
    ],
    "systems administrator": [
        "linux", "windows server", "networking", "scripting", "active directory",
        "monitoring", "backup and recovery", "security", "virtualization", "troubleshooting",
        "automation", "cloud basics"
    ],
    "it support specialist": [
        "troubleshooting", "windows", "networking", "communication", "hardware",
        "active directory", "ticketing systems", "linux", "documentation", "customer service",
        "cybersecurity awareness", "remote support tools"
    ],
    "technical writer": [
        "documentation", "communication", "markdown", "git", "api documentation",
        "editing", "research", "content management", "html", "collaboration",
        "api tools", "version control workflows"
    ],
    "scrum master": [
        "agile", "scrum", "communication", "stakeholder management",
        "leadership", "conflict resolution", "facilitation",
        "documentation", "prioritization", "collaboration",
        "metrics tracking", "coaching"
    ],
    "solutions architect": [
        "system design", "cloud platforms", "communication", "networking",
        "security", "stakeholder management", "databases", "microservices",
        "leadership", "cost optimization",
        "architecture patterns", "integration patterns"
    ],
    "ai engineer": [
        "python", "machine learning", "deep learning", "llms", "prompt engineering",
        "mlops", "rest apis", "data pipelines", "git", "system design",
        "vector databases", "rag", "model evaluation"
    ],
    "nlp engineer": [
        "python", "nlp", "deep learning", "transformers", "hugging face",
        "machine learning", "data pipelines", "statistics", "git", "communication",
        "text preprocessing", "evaluation metrics"
    ],
    "computer vision engineer": [
        "python", "opencv", "deep learning", "tensorflow", "pytorch",
        "image processing", "machine learning", "git", "c++", "data pipelines",
        "image annotation", "model deployment"
    ],
    "data governance analyst": [
        "sql", "data quality", "documentation", "communication",
        "data cataloging", "compliance", "stakeholder management",
        "excel", "reporting", "policy development",
        "data lineage", "metadata management"
    ],
    "growth hacker": [
        "data analysis", "a/b testing", "sql", "marketing analytics",
        "python", "communication", "seo", "experimentation", "excel", "user research",
        "product analytics tools", "conversion optimization"
    ],
    "digital marketing analyst": [
        "google analytics", "seo", "sql", "data visualization", "excel",
        "communication", "a/b testing", "marketing analytics", "social media", "reporting",
        "paid ads platforms", "conversion tracking"
    ],
    "prompt engineer": [
        "llms", "prompt engineering", "python", "communication", "nlp",
        "data analysis", "critical thinking", "rest apis", "documentation", "experimentation",
        "evaluation frameworks", "rag systems", "llm safety"
    ],
    "platform engineer": [
        "kubernetes", "docker", "ci/cd", "terraform", "python", "linux",
        "cloud platforms", "monitoring", "git", "system design",
        "developer experience", "internal tooling"
    ],
    "security engineer": [
        "python", "networking", "encryption", "vulnerability assessment",
        "linux", "firewalls", "incident management", "authentication",
        "security", "threat analysis",
        "secure coding", "threat modeling"
    ],
    "firmware engineer": [
        "c", "c++", "microcontrollers", "rtos", "debugging",
        "communication protocols", "linux", "git",
        "low-level programming", "embedded systems",
        "hardware debugging", "memory management"
    ]
}
PINECONE_INDEX_NAME = "company-knowledge-rag"

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-5.4-mini"

CHUNK_SIZE = 100
CHUNK_OVERLAP = 20

TEST_PDF_PATH = "documents/leave_policy.pdf"

DOCUMENT_CONFIG = {
    "leave_policy.pdf": {
        "document_type": "leave_policy",
        "department": "HR",
        "version": "2026.1",
        "allowed_roles": ["employee", "hr_manager", "it_admin", "security_admin"],
    },
    "employee_handbook.pdf": {
        "document_type": "employee_handbook",
        "department": "HR",
        "version": "2022.4",
        "allowed_roles": ["employee", "hr_manager", "it_admin", "security_admin"],
    },
    "IT_policy.pdf": {
        "document_type": "IT_policy",
        "department": "IT",
        "version": "2023.2",
        "allowed_roles": ["employee", "hr_manager", "it_admin", "security_admin"],
    },
    "onboarding.pdf": {
        "document_type": "onboarding",
        "department": "Office",
        "version": "2023.8",
        "allowed_roles": ["employee", "hr_manager"],
    },
    "security_policy.pdf": {
        "document_type": "security_policy",
        "department": "IT",
        "version": "2026.2",
        "allowed_roles": ["hr_manager", "it_admin", "security_admin"],
    },
}

DOCUMENTS_PATH = "../documents"

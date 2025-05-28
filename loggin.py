import logging

# 로그 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    result = a + b
    logging.info(f"Result: {result}")
    return result

def subtract(a, b):
    logging.info(f"Subtracting {b} from {a}")
    result = a - b
    logging.info(f"Result: {result}")
    return result

# 시범 실행
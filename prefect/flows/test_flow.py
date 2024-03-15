import prefect
from prefect import flow, get_run_logger
from platform import node, platform, python_version


@flow
def test_flow(user_input: str = "World") -> None:
    logger = get_run_logger()
    logger.info(f"Hello {user_input}! 🚀")
    logger.info(f"Network: {node()}. Instance: {platform()}. Agent is healthy 😊")
    logger.info(f"Python version = {python_version()}. Prefect version = {prefect.__version__}. 🐍")


if __name__ == "__main__":
    test_flow("Main")
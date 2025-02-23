from benchmark_run_config.benchmark_run_config import BenchmarkRunConfig


if __name__ == "__main__":
    # Пример использования
    config = BenchmarkRunConfig(
        dataset="Passport_MINI",
        framework="Hugging Face",
        model_name="Qwen2-VL-2B",
        model_family="Qwen2-VL",
        task_name="VQA",
        prompt_collection="AntonShiryaev.csv",
        docker_image="ghcr.io/vlmhyperbenchteam/qwen2-vl:ubuntu22.04-cu124-torch2.4.0_v0.1.0",
        python_package="model_qwen2-vl",
        module="models",
        class_name="Qwen2VL_model",
    )

    print(config)
    
    config.metric_file = 'snils_MODELFRAMEWORK_Qwen2.5-VL-3B-Instruct_VQA_answers_20250223_201510.csv'

    # Сохраняем объект в JSON-файл
    config.to_json("BenchmarkRunConfig.json")

    # Загружаем объект из JSON-файла
    loaded_config = BenchmarkRunConfig.from_json("BenchmarkRunConfig.json")
    print(loaded_config)

    print(config == loaded_config)
import json
from typing import Dict, Any

CATEGORIAS_PERMITIDAS = ["Suporte", "Vendas", "Financeiro", "Geral"]

def parse_json_response(response: str) -> Dict[str, Any]:
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON inválido: {str(e)}")

def validate_schema(data: Dict[str, Any]) -> None:
    if "categoria" not in data:
        raise ValueError("Campo 'categoria' não encontrado.")
    
    if not isinstance(data["categoria"], str):
        raise ValueError("'categoria' deve ser uma string.")

def validate_category(data: Dict[str, Any]) -> None:
    categoria = data["categoria"]

    if categoria not in CATEGORIAS_PERMITIDAS:
        raise ValueError(f"Categoria inválida: {categoria}")

def safe_fallback() -> Dict[str, Any]:
    return {
        "categoria": "Geral",
        "confidence": 0.0,
        "fallback": True
    }

def validate_response(response: str) -> Dict[str, Any]:
    try:
        parsed = parse_json_response(response)
        validate_schema(parsed)
        validate_category(parsed)

        return {
            "categoria": parsed["categoria"],
            "confidence": 1.0,
            "fallback": False
        }

    except Exception as e:
        print(f"[ERRO] {str(e)}")
        return safe_fallback()
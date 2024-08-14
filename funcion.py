import json

def lambda_handler(event, context):
    # Política de tratamiento de datos (puede ser un texto más largo en la práctica)
    data_policy = """
    By using this service, you agree to our data policy:
    - We collect and store personal data for service improvements.
    - Your data will not be shared with third parties without consent.
    - You can review the full policy at our website.
    """
    
    # Simulación de la aceptación del usuario (en un entorno real, esto vendría del front-end)
    user_acceptance = event.get("user_acceptance", "no")

    if user_acceptance.lower() == "yes":
        return {
            'statusCode': 200,
            'body': json.dumps('User accepted the data policy.')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('User did not accept the data policy.')
        }

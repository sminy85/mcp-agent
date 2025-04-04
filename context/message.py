from datetime import datetime

def create_message(sender, recipient, context):
    return {
        "sender": sender,
        "recipient": recipient,
        "context": {
            **context,
            "timestamp": datetime.now().isoformat()
        }
    }

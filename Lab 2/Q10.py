def build_message(**info):
    message_parts = []
    for key, value in info.items():
        message_parts.append(f"{key}: {value}")
    return ', '.join(message_parts)

message = build_message(name="Alice", age=30, city="New York", profession="Engineer")
print(message)

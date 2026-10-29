
from fastapi_mail import  FastMail, MessageSchema, MessageType,NameEmail
from backend.utils.schema import EmailSchema,conf

async def simple_send(persons: EmailSchema) :
    recipient_list = [p.email for p in persons]
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=recipient_list,
        body="<p>Thanks for using Fastapi-mail</p>",
        subtype=MessageType.html,
    )
    print(message)
    await FastMail(conf).send_message(message)
    return {"status":"200","message": "email has been sent"}

# print(simple_send([NameEmail(name="Liteesh",email="liteeshreddyonline@gmail.com")]))
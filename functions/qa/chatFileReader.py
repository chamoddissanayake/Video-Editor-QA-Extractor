import tkinter.messagebox


def readChatFile(chat_file_path):
    chatArr = []

    try:
        with open(chat_file_path) as f:
            lines = f.readlines()
            for row in lines:
                askedTime = row[:8]
                rest = row[9:].strip()
                msg = rest.split(":")[1].strip()
                mgsTo = rest.split(":")[0].strip().split('to')[1].strip()
                msgFrom = rest.split(":")[0].strip().split('to')[0].strip().replace('From', '').strip()

                chatArr.append(
                    {
                        "timestamp":askedTime,
                        "from":msgFrom,
                        "to":mgsTo,
                        "msg":msg
                    }
                )
        return chatArr
    except:
        tkinter.messagebox.showinfo(title='Error', message='Not a valid zoom chat export file.')
        return None
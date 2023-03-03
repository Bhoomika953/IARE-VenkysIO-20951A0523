def reverse(p):
    if len(p) == 0:
        return ""
    else:
        return p[-1] + reverse(p[:-1])


def Rev(para):
    word = para.split()
    rw = [reverse(i) for i in word]
    return " ".join(rw)


para = input("Enter a Paragraph:")
print(Rev(para))

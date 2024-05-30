


def main():


    friends={

        "AJK":20,
        "ravi":21,
        "kushal":21,
    }

    con={

        "yash":23,
        "krish":21,
        "ajay":323,
        **friends
    }

    print(con)


if __name__=="__main__":

    main()
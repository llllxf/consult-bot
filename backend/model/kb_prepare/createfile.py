
import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame(pd.read_excel("../../resource/neo4j.xlsx",sheet_name="goods"))
    with open("test.txt","w") as fw:
        keys = df.keys()
        values = df.values
        fw.writelines(' '.join(str(i) for i in keys)+"@\\")
        fw.writelines("\n")

        for i in values:
            """
            if not pd.isnull(i[6]):
                i[6] = int(i[6])
            """
            s = ' '.join(str(j) for j in i)
            fw.write(s+"@\\")
            fw.writelines("\n")
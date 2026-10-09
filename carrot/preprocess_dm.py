import pandas as pd


def main(date_field, output_field, dm_fp, output):
    df = pd.read_csv(dm_fp, dtype=str)
    df[output_field] = df.apply(lambda x: calc_birth_date(x[date_field], x["AGE"]), axis=1)
    df.to_csv(output, index=False)

def calc_birth_date(date, age):
    return str(int(date[:4]) - int(age[:-2])) + date[4:10]


if __name__ == "__main__":
    date_field = "DMDTC"
    output_field = "CALCBIRTHDTC"
    
    dm_fp = "/home/ubuntu/data/sdtm/dm.csv"
    output = "/home/ubuntu/data/sdtm/dm_birth.csv"
    
    main(date_field, output_field, dm_fp, output)
import psycopg2
import csv

def main():
    host = "postgres"
    database = "postgres"
    user = "postgres"
    pas = "postgres"
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # your code here
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE products(
                    product_id INT
                    ,product_code TEXT
                    ,product_description TEXT
                    ,PRIMARY KEY(product_id)
                );

                CREATE TABLE accounts(
                    customer_id INT
                    ,first_name TEXT
                    ,last_name TEXT
                    ,address_1 TEXT
                    ,address_2 TEXT
                    ,city TEXT
                    ,state TEXT
                    ,zip_code TEXT
                    ,join_date DATE
                    ,PRIMARY KEY(customer_id)
                );

                CREATE TABLE transactions(
                    transaction_id TEXT
                    ,transaction_date DATE
                    ,product_id INT
                    ,product_code TEXT
                    ,product_description TEXT
                    ,quantity INT
                    ,account_id INT
                    ,PRIMARY KEY(transaction_id)
                    ,CONSTRAINT fk_account_id
                        FOREIGN KEY(account_id)
                        REFERENCES accounts(customer_id)
                    ,CONSTRAINT fk_product_id
                        FOREIGN KEY(product_id)
                        REFERENCES products(product_id)
                );
                """)
    conn.commit()
    with open('data/accounts.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'accounts', sep=',')
    with open('data/products.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'products', sep=',')
    with open('data/transactions.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'transactions', sep=',')
    conn.commit()

if __name__ == "__main__":
    main()

# Proof of Concept of Beancount Error

This repro shows an apparent bug in Beancount 2.3.4 where Beancount fails to import a transaction.

## Demo

You can reproduce this issue under Docker:

```bash
cd $(mktemp -d) && \
  git clone https://github.com/mtlynch/beancount-repro.git . && \
  sudo docker build -t beancount . && \
  sudo docker run -it -v "${PWD}:/app" -w /app --entrypoint /app/repro beancount
```

### Expected

```text
2021-12-02 * "Dummy Payee" ""
  Assets:Checking  1868.26 USD
  Income:Dummy
```

### Actual

Blank output

## Notes

If you change certain values, you get the correct output. For example:

* Changing the `1779.31` in `repro.beancount` to `21779.31` causes the script to yield the correct output.
* Changing the date on the transaction in `csv.py` to `date=datetime.date(2021, 10, 2)` causes the script to yield the correct output.
* Changing the amount on the transaction in `csv.py` to `number.D('21868.26')` causes the script to yield the correct output.

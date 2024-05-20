# uddr_log_converter

The purpose of this project is to convert common log-type files into a format that is suitable for [UltraDDR's log runner API](https://api.ddr.ultradns.com/docs/ultraddr/#/DNS%20Log%20Runner%20API/submitUsingPOST). Currently, it only supports BIND query logs.

## BIND Logs

You can see an example of the BIND server `queries_log` format in the `examples` directory. This logging must be enabled in the server's options:

```
channel queries_log {
  file "/var/named/log/queries/named.log" versions 600 size 20m;
  print-time yes;
  print-category yes;
  print-severity yes;
  severity info;
};
```

## Usage

The script takes the input file as an argument. It will produce an output of the same name, appended with `_converted.csv`.

1. Clone this repository:

    ```sh
    git clone https://github.com/sbarbett/uddr_log_converter.git
    cd uddr_log_converter
    ```

2. Make the script executable:

    ```sh
    chmod +x src/convert.py
    ```

3. Run it:

	```sh
	./src/convert.py examples/bind-queries.log
	```

The output should be:

```
Log file 'examples/bind-queries.log' has been converted to CSV format and saved as 'examples/bind-queries.log_converted.csv'.
```
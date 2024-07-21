## Downloader

To generate the plots, you'll need the USHCN datafiles. These are published
by NOAA, but not in a form that can be used directly. So I've written a simple
application to allow you to do it yourself.

It's available here: [crates.io](https://crates.io/crates/ushcn).

It's a terminal command line application, written in Rust. To use it, you'll
need to install Rust, then install the application, then run it periodically.

Here's how to install it. First, install rust:

```bash
> curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Then install the application:

```bash
> cargo install ushcn
```

Then run it:

```bash
> ushcn daily
```

That will download the latest datafiles from the USHCN FTP site and save them to
your home directory.

## Plotting scripts

To run the scripts yourself, download the repository from
GitHub: [https://github.com/rjl-climate/USHCN-temperatures/tree/main](
https://github.com/rjl-climate/USHCN-temperatures/tree/main).

Edit the script at `utils/data.py` and edit the variables
`daily_parquet_file_path` and `monthly_parquet_file_path` to point to where you've
downloaded the data (see above). Then you can
run the scripts in the `plots` directory.
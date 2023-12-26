import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")  # extra value
parser.add_argument(
    "-f", "--fast", dest="fast", action="store_true"
)  # existence/nonexistence
args = parser.parse_args()

print(args.decimal)
print(args.fast)


# parser = argparse.ArgumentParser()

# parser.add_argument(dest="dst", action="store")
# parser.add_argument("--qp", dest="qp", action="store")
# parser.add_argument("--configure", dest="configure", action="store")
# args = parser.parse_args()

# print(args.dst)
# print(args.qp)
# print(args.configure)

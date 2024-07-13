from shlex import join


def main():
    nums = []
    for i in range(2000, 3001):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(str(i))
    print(",".join(nums))

if __name__ == "__main__":
    main()
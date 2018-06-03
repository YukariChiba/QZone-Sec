from tqdm import tqdm


def pr_red(skk): tqdm.write("\033[91m {}\033[00m" .format(skk))


def pr_green(skk): tqdm.write("\033[92m {}\033[00m" .format(skk))


def pr_yellow(skk): tqdm.write("\033[93m {}\033[00m" .format(skk))


def pr_light_purple(skk): tqdm.write("\033[94m {}\033[00m" .format(skk))


def pr_purple(skk): tqdm.write("\033[95m {}\033[00m" .format(skk))


def pr_cyan(skk): tqdm.write("\033[96m {}\033[00m" .format(skk))


def pr_light_gray(skk): tqdm.write("\033[97m {}\033[00m" .format(skk))


def pr_black(skk): tqdm.write("\033[98m {}\033[00m" .format(skk))

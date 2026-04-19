def secure_archive(fd: str, action: int, content: str) -> tuple[bool, str]:
    try:
        if action == 0:
            with open(fd) as file:
                data = file.read()
        elif action == 1:
            with open(fd, "w") as file:
                file.write(content)
                data = "Content successfully written to file"
        return (True, data)
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print()

    script = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive("/not/existing/file", 0, "")}")
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive("/etc/master.passwd", 0, "")}")
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive("ancient_fragment.txt", 0, "")}")
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{secure_archive("ancient_fragment.txt", 1, script)}")


if __name__ == "__main__":
    ft_vault_security()

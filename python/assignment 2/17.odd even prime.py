

# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

def is_prime(num):
  
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    even_numbers = [num for num in range(1, 101) if num % 2 == 0]
    odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
    prime_numbers = [num for num in range(1,101) if is_prime(num)]

    print("List of even numbers:", even_numbers)
    print("List of odd numbers:", odd_numbers)
    print("List of prime numbers:", prime_numbers)

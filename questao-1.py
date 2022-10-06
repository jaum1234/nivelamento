numbers = [1, 7, 2, 9];

def sequence(numbers):
    if(len(numbers) == 100):
        return numbers;
    
    numbers.append(numbers[len(numbers) - 3] + numbers[len(numbers) - 4]);
    
    sequence(numbers);
    
sequence(numbers);

print(numbers);
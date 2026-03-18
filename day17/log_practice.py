import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("number_loop")

def number_loop(numbers):
    if numbers:
        if len(numbers) <= 3:
            logger.warning("3 or less numbers in list")
        else:
            count = 0
            for i in range(5):
                new_number = numbers[count] + 1
                logger.debug(f"{numbers[count]} is being changed to {new_number}")
                numbers[count] = new_number
                count += 1
            logger.info(f"Finished numbers list: {numbers}")
            logger.debug(f"Count total: {count}")
            return numbers
    else:
        logging.error("No numbers list found for number_loop")

numbers_list = [1, 4, 6 , 8, 88, 54, 3]
numbers_list_two = [3, 5 , 1]

number_loop(numbers_list_two)





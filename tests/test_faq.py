import allure
import pytest
from config.config import FAQData
from pages.home_page import HomePage

@allure.feature('FAQ раздел')
class TestFAQ:
    
    @allure.title('Проверка ответов на вопросы в FAQ')
    @allure.description('Проверяем корректность текста ответов на все вопросы')
    @pytest.mark.parametrize('question_index, expected_answer', 
                           enumerate(FAQData.ANSWERS))
    def test_faq_answers(self, setup_driver, question_index, expected_answer):
        home_page = HomePage(setup_driver)
        home_page.accept_cookies()
        
        actual_answer = home_page.get_faq_answer(question_index)
        assert actual_answer == expected_answer, \
            f"Неверный ответ на вопрос {question_index + 1}"

from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
import time

# Opcional - Mantener el navegador abierto (ayuda a diagnosticar problemas si el script falla)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


def init_driver():
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://orteil.dashnet.org/experiments/cookie/")
        return driver
    except Exception as e:
        print(f"Error al iniciar el navegador: {e}")
        return None

def init_db():
    conn = sqlite3.connect('instance/cookie_clicker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cookies_per_second (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cps TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

driver = init_driver()
if driver is None:
    exit(1)

# conecta con la base de datos
db_conn = init_db()
db_cursor = db_conn.cursor()

def get_item_prices():
    try:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        return item_prices
    except Exception as e:
        print(f"Error al obtener precios: {e}")
        return []

try:
    cookie = driver.find_element(by=By.ID, value="cookie")
except Exception as e:
    print(f"Error al encontrar el elemento de la galleta: {e}")
    driver.quit()
    exit(1)

# obtiene los ids de los datros de mejoras
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5
cps_log = []
purchased_items = set()

try:
    while True:
        try:
            cookie.click()

            if time.time() > timeout:
                cookie_upgrades = {}
                item_prices = get_item_prices()

                for n in range(len(item_prices)):
                    cookie_upgrades[item_prices[n]] = item_ids[n]

                money_element = driver.find_element(by=By.ID, value="money").text
                if "," in money_element:
                    money_element = money_element.replace(",", "")
                cookie_count = int(money_element)


                affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost and id not in purchased_items}

                if affordable_upgrades:
                    highest_cps_upgrade = max(affordable_upgrades.items(), key=lambda item: driver.find_element(by=By.ID, value=item[1]).text.split("\n")[1])
                    print(f"Comprando: {highest_cps_upgrade[1]} por {highest_cps_upgrade[0]}")
                    driver.find_element(by=By.ID, value=highest_cps_upgrade[1]).click()
                    purchased_items.add(highest_cps_upgrade[1])  # Agregar a los objetos comprados

                timeout = time.time() + 5

            if time.time() > five_min:
                cookie_per_s = driver.find_element(by=By.ID, value="cps").text
                cps_log.append(cookie_per_s)
                print(f"Cookies por segundo: {cookie_per_s}")


                db_cursor.execute("INSERT INTO cookies_per_second (cps) VALUES (?)", (cookie_per_s,))
                db_conn.commit()

                break

        except Exception as e:
            print(f"Error durante la ejecución del script: {e}")
            driver.quit()
            exit(1)

except KeyboardInterrupt:
    print("El programa se detuvo.")
finally:
    driver.quit()
    db_conn.close()  #

print("Registro de Cookies por segundo durante el tiempo de ejecución:")
for cps in cps_log:
    print(cps)

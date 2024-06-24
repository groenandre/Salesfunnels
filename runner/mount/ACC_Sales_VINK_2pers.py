import re
import shared
from playwright.sync_api import Page, expect

bsn_nummer_een = shared.generate_valid_bsn()
bsn_nummer_twee = shared.generate_valid_bsn()

def test_example(page: Page) -> None:
    page.goto("https://www2.acc.vinkvink.nl/premie-berekenen-en-aanvragen")
    page.get_by_role("button", name="Accepteren").click()
    #Aantal verzekerdem
    page.get_by_role("button", name="+").nth(1).click()
    page.click("#volgende-stap")
    #Basisverzekering
    page.get_by_text("€ 485").click()
    page.click("#volgende-stap")
    #Aanvullende verzekering
    page.click('button[value*="|VBT|Aanvullendproduct"]')
    page.click("#volgende-stap")
    #page.click("#kiesGeenUpsellButton")
    #Gegevens
    page.locator("//input[contains(@id,'Verzekerden_0__Aanhef_Value_Man')]/ancestor::div[contains(@class,'input-radio')]").click()
    page.locator("#Verzekerden_0__Voorletters_Value").fill("a")
    page.locator("#Verzekerden_0__Achternaam_Value").fill("vinkautotwee")
    #functie voor BSN
    page.locator("#Verzekerden_0__BurgerServiceNummer_Value").fill(bsn_nummer_een)
    page.locator("#Verzekerden_0__Geboortedatum_Value_Day").fill("1")
    page.locator("#Verzekerden_0__Geboortedatum_Value_Month").fill("6")
    page.locator("#Verzekerden_0__Geboortedatum_Value_Year").fill("1978")
    #refresh na geboortedatum velden
    page.wait_for_selector("#Verzekerden_0__EmailAdres_Value")
    expect(page.locator("#Verzekerden_0__EmailAdres_Value")).to_be_visible()
    page.locator("#Verzekerden_0__Telefoonnummer_Value").fill("0612345678")
    #Medeverzekerde
    page.locator("//input[contains(@id,'Verzekerden_1__Aanhef_Value_Man')]/ancestor::div[contains(@class,'input-radio')]").click()
    page.locator("#Verzekerden_1__Voorletters_Value").fill("b")
    page.locator("#Verzekerden_1__Achternaam_Value").fill("vinkautotwee")
    #functie voor BSN aanmaken
    page.locator("#Verzekerden_1__BurgerServiceNummer_Value").fill(bsn_nummer_twee)
    page.locator("#Verzekerden_1__Geboortedatum_Value_Day").fill("1")
    page.locator("#Verzekerden_1__Geboortedatum_Value_Month").fill("3")
    page.locator("#Verzekerden_1__Geboortedatum_Value_Year").fill("2023")
    #Adres
    page.locator("#Adres_PostCode_Value").fill("9723AB")
    page.locator("#Adres_Huisnummer_Value").fill("70")
    #Email en IBAN (moet later ivm refresh)
    page.locator("#Verzekerden_0__EmailAdres_Value").fill("output.webtesten@menzis.nl")
    page.locator("#Verzekerden_0__HerhaalEmailAdres_Value").fill("output.webtesten@menzis.nl")
    page.locator("#Verzekerden_0__IBAN_Value").fill("NL33TEST0914505688")
    page.click("#volgende-stap")
    #Inschrijfreden en verzend aanvraag
    #page.get_by_label("Inschrijfreden").select_option("003")
    page.get_by_label("Inschrijfreden").select_option("007")
    page.click("#volgende-stap")
    #time out moet weg na debuggen
    #page.wait_for_timeout(10000)

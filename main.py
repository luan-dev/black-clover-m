import os

import pyautogui


# time.sleep(random.uniform(click_delay - 0.1, click_delay + 0.1))
def locate_asta():
    CONFIDENCE = 0.69
    MIN_SEARCH_TIME = 0.5

    cwd = os.getcwd()
    assets_path = os.path.join(cwd, "assets")

    asta_coords = None
    asta_right_path = os.path.join(assets_path, "asta-right.png")
    asta_face_rock_path = os.path.join(assets_path, "asta-face-rock.png")
    asta_away_rock_path = os.path.join(assets_path, "asta-away-rock.png")

    try:
        asta_right = pyautogui.locateOnScreen(
            asta_right_path,
            confidence=CONFIDENCE,
            minSearchTime=MIN_SEARCH_TIME,
        )
        asta_coords = asta_right
        print("asta is facing the right")
    except Exception:
        pass

    try:
        asta_fack_rock = pyautogui.locateOnScreen(
            asta_face_rock_path,
            confidence=CONFIDENCE,
            minSearchTime=MIN_SEARCH_TIME,
        )
        asta_coords = asta_fack_rock
        print("asta is facing the rock")
    except Exception:
        pass

    try:
        asta_away_rock = pyautogui.locateOnScreen(
            asta_away_rock_path,
            confidence=CONFIDENCE,
            minSearchTime=MIN_SEARCH_TIME,
        )
        asta_coords = asta_away_rock
        print("asta is facing away from the rock")
    except Exception:
        pass

    print(asta_coords)


def main():
    print("Black Clover M - Asta's Extra Training")
    print("--------------------------------------")

    locate_asta()


if __name__ == "__main__":
    main()

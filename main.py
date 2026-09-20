import argparse
import cv2

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def blur_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for x, y, w, h in cascade.detectMultiScale(gray, 1.1, 5, minSize=(40, 40)):
        k = (w // 3) | 1  # odd kernel size scaled to face
        frame[y:y + h, x:x + w] = cv2.GaussianBlur(frame[y:y + h, x:x + w], (k, k), 30)
    return frame


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image")
    p.add_argument("--output", help="save blurred image here")
    args = p.parse_args()
    if args.image:
        img = cv2.imread(args.image)
        if img is None:
            raise SystemExit(f"Could not read {args.image}")
        img = blur_faces(img)
        if args.output:
            cv2.imwrite(args.output, img)
            print("Saved", args.output)
        cv2.imshow("Face Blurring", img)
        cv2.waitKey(0)
    else:
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ok, frame = cap.read()
            if not ok:
                break
            cv2.imshow("Face Blurring", blur_faces(frame))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

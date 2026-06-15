from pipeline.extract import extract_from_excel
from pipeline.transform import contact_data_frames
from pipeline.load import load_excel

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(type(data_frame_list))
    data_frame = contact_data_frames(data_frame_list)
    print(type(data_frame))
    load_excel(data_frame, "data/output", "output")
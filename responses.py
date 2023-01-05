import time


def response(intents):
    if intents == "giam ho":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký làm người giám hộ,
        bạn có thể nhấn vào link bên cạnh để tìm hiểu thêm. Xin cảm ơn!"""
        thu_tuc = ["Giấy tờ phải nộp:",
                   "- Văn bản cử người giám hộ theo quy định của Bộ luật Dân sự đối với trường hợp đăng ký giám hộ cử. (1 bản chính)",
                   "- Giấy tờ chứng minh điều kiện giám hộ đương nhiên theo quy định của Bộ luật Dân sự đối với trường hợp đăng ký giám hộ đương nhiên. Trường hợp có nhiều người cùng đủ điều kiện làm giám hộ đương nhiên thì nộp thêm văn bản thỏa thuận về việc cử một người làm giám hộ đương nhiên. (1 bản chính)",
                   "- Văn bản ủy quyền theo quy định của pháp luật trong trường hợp ủy quyền thực hiện việc đăng ký giám hộ. Trường hợp người được ủy quyền là ông, bà, cha, mẹ, con, vợ, chồng, anh, chị, em ruột của người ủy quyền thì văn bản ủy quyền không phải chứng thực. (1 bản chính)",
                   "(Phía dưới là tờ khai đăng ký giám hộ theo mẫu)",
                   "*Người có yêu cầu đăng ký giám hộ nộp hồ sơ đăng ký giám hộ tại Bộ phận một cửa của UBND cấp xã/phường có thẩm quyền;nộp lệ phí nếu thuộc trường hợp phải nộp lệ phí đăng ký giám hộ; nộp phí cấp bản sao Trích lục đăng ký giám hộnếu có yêu cầu cấp bản sao Trích lục đăng ký giám hộ.",
                   "*Có thể thực hiện đăng ký giám hộ qua hình thức trực tuyến."]
        link = [["Thông tin đầy đủ hơn", "https://dichvucong.gov.vn/p/home/dvc-tthc-thu-tuc-hanh-chinh-chi-tiet.html?ma_thu_tuc=6763"],
                ["Mẫu tờ khai đăng ký giám hộ", "https://docs.google.com/document/d/1z4GrF_kFKVURcz3T6shS158J3N5Vp6BO/edit"]]

    elif intents == "ket hon":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký kết hôn,
        bạn có thể nhấn vào link bên cạnh để tìm hiểu thêm. Xin cảm ơn!"""
        thu_tuc = ["- Có 2 hình thức đăng ký kết hôn là nộp hồ sơ trực tiếp và nộp hồ sơ trực tuyến",
                   "+ Nếu lựa chọn hình thức nộp hồ sơ trực tiếp, người có yêu cầu đăng ký kết hôn nộp hồ sơ đăng ký kết hôn tại Bộ phận một cửa của UBND cấp xã/phường có thẩm quyền; nộp lệ phí nếu thuộc trường hợp phải nộp lệ phí đăng ký kết hôn; nộp phí cấp bản sao Trích lục kết hôn nếu có yêu cầu cấp bản sao Trích lục kết hôn.",
                   "+ Nếu lựa chọn hình thức nộp hồ sơ trực tuyến, người có yêu cầu đăng ký kết hôn truy cập Cổng dịch vụ công quốc gia hoặc Cổng dịch vụ công cấp tỉnh, đăng ký tài khoản (nếu chưa có tài khoản), xác thực người dùng theo hướng dẫn, đăng nhập vào hệ thống, xác định đúng Ủy ban nhân dân cấp xã có thẩm quyền.",
                   "- Giấy tờ phải nộp:",
                   "+ Bản chính Giấy xác nhận tình trạng hôn nhân do Ủy ban nhân dân cấp xã có thẩm quyền cấp trong trường hợp người yêu cầu đăng ký kết hôn không đăng ký thường trú tại địa bàn xã, phường, thị trấn làm thủ tục đăng ký kết hôn. (1 bản chính)",
                   "- Giấy tờ phải xuất trình:",
                   "+ Hộ chiếu hoặc Chứng minh nhân dân hoặc Thẻ căn cước công dân hoặc các giấy tờ khác có dán ảnh và thông tin cá nhân do cơ quan có thẩm quyền cấp, còn giá trị sử dụng để chứng minh về nhân thân của người có yêu cầu đăng ký khai sinh.",
                   "+ Giấy tờ chứng minh nơi cư trú."]
        link = [["Thông tin đầy đủ hơn", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.000894"],
                ["Mẫu đơn đăng ký kết hôn", "https://docs.google.com/document/d/1Lvy9V3SuvraNlYlAO4OzBmFhSqgSVp1f/edit"]]

    elif intents == "dang ky nvqs":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký thực hiện Nghĩa vụ quân sự."""
        thu_tuc = ["- Trình tự thực hiện đăng ký nghĩa vụ quân sự gồm 3 bước:",
                   "+ Bước 1: Trước thời hạn 10 ngày, tính đến ngày đăng ký nghĩa vụ quân sự, Ban Chỉ huy quân sự cấp xã có trách nhiệm chuyển Lệnh gọi đăng ký nghĩa vụ quân sự đến công dân. Trường hợp cơ quan, tổ chức không có Ban Chỉ huy quân sự, thì người đứng đầu hoặc người đại diện hợp pháp của cơ quan, tổ chức có trách nhiệm chuyển Lệnh gọi đăng ký nghĩa vụ quân sự đến công dân",
                   "+ Bước 2: Sau khi nhận được Lệnh gọi đăng ký nghĩa vụ quân sự của Chỉ huy trưởng Ban Chỉ huy quân sự huyện, quận, thị xã, thành phố thuộc tỉnh và đơn vị hành chính tương đương (sau đây gọi chung là Chỉ huy trưởng Ban Chỉ huy quân sự cấp huyện) công dân có trách nhiệm đến Ban Chỉ huy quân sự xã, phường, thị trấn, cơ quan, tổ chức (sau đây gọi chung là Ban Chỉ huy quân sự cấp xã) để trực tiếp đăng ký nghĩa vụ quân sự.",
                   "+ Bước 3: Trong thời hạn 01 ngày, Ban Chỉ huy quân sự cấp xã có trách nhiệm đối chiếu bản gốc giấy chứng minh nhân dân hoặc giấy khai sinh; hướng dẫn công dân kê khai Phiếu tự khai sức khỏe nghĩa vụ quân sự, đăng ký các thông tin cần thiết của công dân vào Sổ danh sách công dân nam đủ 17 tuổi trong năm, Sổ đăng ký công dân sẵn sàng nhập ngũ và chuyển Giấy chứng nhận đăng ký nghĩa vụ quân sự cho công dân ngay sau khi đăng ký.",
                   "- Giấy tờ cần chuẩn bị:",
                   "+ Phiếu tự khai sức khỏe nghĩa vụ quân sự (1 bản chính)",
                   "+ Bản chụp giấy chứng minh nhân dân hoặc giấy khai sinh (1 bản sao) (mang theo bản chính để đối chiếu)",
                   "- Để thực nghĩa vụ quân sự, bạn phải có đủ các điều kiện sau:",
                   "+ Công dân nam đủ 17 tuổi trở lên.",
                   "+ Công dân nữ đủ 18 tuổi trở lên có ngành, nghề chuyên môn phù hợp với yêu cầu của Quân đội nhân dân theo hướng dẫn tại Nghị định 14/2016/NĐ-CP như thạc sĩ báo chí học, truyền thông đại chúng, kế toán,….",
                   "- Các đối tượng không đủ điều kiện đăng ký nghĩa vụ quân sự:",
                   "+ Người đang bị áp dụng biện pháp giáo dục tại xã, phường, thị trấn (sau đây gọi chung là cấp xã) hoặc đưa vào trường giáo dưỡng, cơ sở giáo dục bắt buộc, cơ sở cai nghiện bắt buộc.",
                   "+ Người đang bị truy cứu trách nhiệm hình sự; đang chấp hành hình phạt tù, cải tạo không giam giữ, quản chế hoặc đã chấp hành xong hình phạt tù nhưng chưa được xóa án tích.",
                   "+ Người bị tước quyền phục vụ trong lực lượng vũ trang nhân dân."
                   ]
        link = [["Thủ tục đăng ký nghĩa vụ quân sự lần đầu", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.001821"],
                ["Thủ tục đăng ký nghĩa vụ quân sự tạm vắng",
                    "https://dichvucong.gov.vn/p/home/dvc-tthc-thu-tuc-hanh-chinh-chi-tiet.html?ma_thu_tuc=2522"],
                ["Thủ tục Đăng ký nghĩa vụ quân sự bổ sung",
                    "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.001771"],
                ["Tiêu chuẩn chiều cao, cân nặng để tham gia NVQS", "https://luatminhkhue.vn/tieu-chuan-chieu-cao--can-nang-de-tham-gia-nghia-vu-quan-su--.aspx#:~:text=TI%C3%8AU%20CHU%E1%BA%A8N%20PH%C3%82N%20LO%E1%BA%A0I%20THEO%20TH%E1%BB%82%20L%E1%BB%B0C%20(B%E1%BA%A3ng%20s%E1%BB%91%201)"]]

    elif intents == "ho ngheo":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký chứng nhận hộ nghèo."""
        thu_tuc = ["- Trình tự thực hiện",
                   "+ Bước 1. Hộ gia đình có giấy đề nghị xét duyệt bổ sung hộ nghèo, hộ cận nghèo nộp trực tiếp hoặc gửi qua bưu điện đến Ủy ban nhân dân cấp xã tiếp nhận, xử lý.",
                   "+ Bước 2. Ủy ban nhân dân cấp xã chỉ đạo Ban giảm nghèo cấp xã lập danh sách các hộ gia đình có giấy đề nghị và tổ chức thẩm định theo mẫu Phiếu B (theo Phụ lục số 3b ban hành kèm theo Thông tư số 17/2016/TT-BLĐTBXH ngày 26/8/2016 của Bộ Lao động - Thương binh và Xã hội); báo cáo kết quả thẩm định và trình Chủ tịch Ủy ban nhân dân cấp xã quyết định công nhận danh sách hộ nghèo, hộ cận nghèo phát sinh; niêm yết công khai danh sách tại trụ sở Ủy ban nhân dân cấp xã.",
                   "Thời gian thẩm định, xét duyệt và ban hành Quyết định công nhận danh sách hộ nghèo, hộ cận nghèo phát sinh không quá 07 ngày làm việc kể từ khi tiếp nhận giấy đề nghị của hộ gia đình. Trường hợp không ban hành Quyết định công nhận thì cần nêu rõ lý do.",
                   "- Giấy tờ cần chuẩn bị:",
                   "+ Giấy đề nghị xét duyệt bổ sung hộ nghèo, hộ cận nghèo (theo mẫu tại Phụ lục số 1a ban hành kèm theo Thông tư số 14/2018/TT-BLĐTBXH ngày 26/9/2018 của Bộ Lao động - Thương binh và Xã hội).",
                   "(Đính kèm link bên dưới)"]
        link = [["Công nhận hộ nghèo, hộ cận nghèo phát sinh trong năm", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.000506"],
                ["Giấy đề nghị xét duyệt bổ sung hộ nghèo, cận nghèo", "https://docs.google.com/document/d/1UMG_sGwWiqMwrKxwnYbTKBHD-DxbJ6yR/edit"]]

    elif intents == "ket hon tam tru":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký kết hôn tại nơi tạm trú."""
        thu_tuc = ["Trường hợp đăng ký kết hôn tại Ủy ban nhân dân cấp xã mà người yêu cầu đăng ký kết hôn không thường trú tại xã, phường, thị trấn nơi đăng ký kết hôn thì phải nộp Giấy xác nhận tình trạng hôn nhân do Ủy ban nhân dân cấp xã có thẩm quyền cấp theo quy định tại các Điều 21, 22 và 23 của Nghị định này.",
                   "Để biết thêm thông tin về thủ tục đăng ký kết hôn đừng ngần ngại hỏi tôi lần nữa nhé"]
        link = [["Thủ tục đăng ký kết hôn", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.000894"],
                ["Một số câu hỏi liên quan đến đăng ký kết hôn", "https://dichvucong.gov.vn/p/home/dvc-ket-qua-thu-tuc.html?originKey=k%E1%BA%BFt%20h%C3%B4n&tukhoa=k%E1%BA%BFt%20h%C3%B4n&tinh_thanh="]]

    elif intents == "tu y ket hon":
        bot_audio = """Chào bạn, việc đăng ký kết hôn giữa nam và nữ có thể thực hiện khi cả hai đều đáp ứng đầy đủ, các điều kiện do nhà nước quy định mà không cần sự cho phép của cha mẹ hai bên."""
        thu_tuc = ["- Điều kiện để đăng ký kết hôn:",
                   "a) Nam từ đủ 20 tuổi trở lên, nữ từ đủ 18 tuổi trở lên",
                   "b) Việc kết hôn do nam và nữ tự nguyện quyết định",
                   "c) Không bị mất năng lực hành vi dân sự",
                   "(Người bị mất năng lực hành vi dân sự là người bị bệnh tâm thần hoặc mắc bệnh khác mà không thể nhận thức, làm chủ được hành vi và được Tòa án ra quyết định tuyên bố người này là người mất năng lực hành vi dân sự trên cơ sở kết luận giám định pháp y tâm thần.)",
                   "d) Việc kết hôn không thuộc một trong các trường hợp cấm kết hôn theo quy định tại các điểm a, b, c và d khoản 2 Điều 5 của Luật này.",
                   "(Những trường hợp cấm kết hôn được quy định tại điểm a, b, c và d khoản 2 Điều 5 của Luật Hôn nhân và Gia đình năm 2014 bao gồm:",
                   "+  Kết hôn giả tạo, ly hôn giả tạo",
                   "+  Tảo hôn, cưỡng ép kết hôn, lừa dối kết hôn, cản trở kết hôn",
                   "+  Người đang có vợ, có chồng mà kết hôn với người khác hoặc chưa có vợ, chưa có chồng mà kết hôn với người đang có chồng, có vợ",
                   "+  Kết hôn giữa những người cùng dòng máu về trực hệ; giữa những người có họ trong phạm vi ba đời; giữa cha, mẹ nuôi với con nuôi; giữa người đã từng là cha, mẹ nuôi với con nuôi, cha chồng với con dâu, mẹ vợ với con rể, cha dượng với con riêng của vợ, mẹ kế với con riêng của chồng.)"
                   "**Lưu ý: Nhà nước không thừa nhận hôn nhân giữa những người cùng giới tính."
                   ]
        link = [["Thủ tục đăng ký kết hôn", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=1.000894"],
                ["Một số câu hỏi liên quan đến đăng ký kết hôn", "https://dichvucong.gov.vn/p/home/dvc-ket-qua-thu-tuc.html?originKey=k%E1%BA%BFt%20h%C3%B4n&tukhoa=k%E1%BA%BFt%20h%C3%B4n&tinh_thanh="]]

    elif intents == "thoi gian nghi ket hon":
        bot_audio = """Chào bạn, Thời gian nghỉ đăng ký kên hôn theo quy định nhà nước là 3 ngày"""
        thu_tuc = ["Theo Điều 115 Bộ luật Lao động năm 2019 quy định trường hợp nghỉ việc riêng, nghỉ không hưởng lương",
                   "Người lao động được nghỉ việc riêng mà vẫn hưởng nguyên lương và phải thông báo với người sử dụng lao động trong trường hợp sau đây:",
                   "a) Kết hôn: nghỉ 03 ngày",
                   "b) Con đẻ, con nuôi kết hôn: nghỉ 01 ngày",
                   "c) Cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi; cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi của vợ hoặc chồng; vợ hoặc chồng; con đẻ, con nuôi mất: nghỉ 03 ngày."]
        link = [["", ""]]

    elif intents == "hoan nvqs":
        bot_audio = """Chào bạn, sau đây là một số trường hợp được hoãn hoặc miễn thực hiện Nghĩa vụ quân sự năm 2023."""
        thu_tuc = ["I) Các trường hợp được tạm hoãn nghĩa vụ quân sự năm 2023:",
                   "(1) Chưa đủ sức khỏe phục vụ tại ngũ theo kết luận của Hội đồng khám sức khỏe",
                   "(2) Là lao động duy nhất phải trực tiếp nuôi dưỡng thân nhân không còn khả năng lao động hoặc chưa đến tuổi lao động; trong gia đình bị thiệt hại nặng về người và tài sản do tai nạn, thiên tai, dịch bệnh nguy hiểm gây ra được Ủy ban nhân dân cấp xã xác nhận",
                   "(3) Một con của bệnh binh, người nhiễm chất độc da cam suy giảm khả năng lao động từ 61% đến 80%",
                   "(4) Có anh, chị hoặc em ruột là hạ sĩ quan, binh sĩ đang phục vụ tại ngũ; hạ sĩ quan, chiến sĩ thực hiện nghĩa vụ tham gia Công an nhân dân",
                   "(5) Người thuộc diện di dân, giãn dân trong 03 năm đầu đến các xã đặc biệt khó khăn theo dự án phát triển kinh tế - xã hội của Nhà nước do Ủy ban nhân dân cấp tỉnh trở lên quyết định",
                   "(6) Cán bộ, công chức, viên chức, thanh niên xung phong được điều động đến công tác, làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn theo quy định của pháp luật",
                   "(7) Đang học tại cơ sở giáo dục phổ thông; đang được đào tạo trình độ đại học hệ chính quy thuộc cơ sở giáo dục đại học, trình độ cao đẳng hệ chính quy thuộc cơ sở giáo dục nghề nghiệp trong thời gian một khóa đào tạo của một trình độ đào tạo.",
                   "(8) Dân quân thường trực.",
                   "II) Các trường hợp được miễn nghĩa vụ quân sự năm 2023:",
                   "(1) Con của liệt sĩ, con của thương binh hạng một",
                   "(2) Một anh hoặc một em trai của liệt sĩ",
                   "(3) Một con của thương binh hạng hai; một con của bệnh binh suy giảm khả năng lao động từ 81% trở lên; một con của người nhiễm chất độc da cam suy giảm khả năng lao động từ 81 % trở lên",
                   "(4) Người làm công tác cơ yếu không phải là quân nhân, Công an nhân dân",
                   "(5) Cán bộ, công chức, viên chức, thanh niên xung phong được điều động đến công tác, làm việc ở vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn theo quy định của pháp luật từ 24 tháng trở lên."]
        link = [["Tiêu chuẩn chiều cao, cân nặng để tham gia NVQS",
                 "https://luatminhkhue.vn/tieu-chuan-chieu-cao--can-nang-de-tham-gia-nghia-vu-quan-su--.aspx#:~:text=TI%C3%8AU%20CHU%E1%BA%A8N%20PH%C3%82N%20LO%E1%BA%A0I%20THEO%20TH%E1%BB%82%20L%E1%BB%B0C%20(B%E1%BA%A3ng%20s%E1%BB%91%201)"]]

    elif intents == "to cao":
        bot_audio = "Chào bạn, sau đây là một số hướng dẫn thực hiện đơn tố cáo tại Ủy ban nhân dân Xã/Phường"
        thu_tuc = ["I) Điều kiện thực hiện:",
                   "1) Người tố cáo có đủ năng lực hành vi dân sự; trường hợp không có đủ năng lực hành vi dân sự thì phải có người đại diện theo quy định của pháp luật;",
                   "2) Vụ việc thuộc thẩm quyền giải quyết tố cáo của cơ quan, tổ chức, cá nhân tiếp nhận tố cáo;",
                   "3) Nội dung tố cáo có cơ sở để xác định người vi phạm, hành vi vi phạm pháp luật.",
                   "Trường hợp tố cáo xuất phát từ vụ việc khiếu nại đã được giải quyết đúng thẩm quyền, trình tự, thủ tục theo quy định của pháp luật nhưng người khiếu nại không đồng ý mà chuyển sang tố cáo người đã giải quyết khiếu nại thì chỉ thụ lý tố cáo khi người tố cáo cung cấp được thông tin, tài liệu, chứng cứ để xác định người giải quyết khiếu nại có hành vi vi phạm pháp luật.",
                   "II) Thực hiện tố cáo:",
                   "1) Trường hợp tố cáo được thực hiện bằng đơn thì trong đơn tố cáo phải ghi rõ ngày, tháng, năm tố cáo; họ tên, địa chỉ của người tố cáo, cách thức liên hệ với người tố cáo; hành vi vi phạm pháp luật bị tố cáo; người bị tố cáo và các thông tin khác có liên quan. Trường hợp nhiều người cùng tố cáo về cùng một nội dung thì trong đơn tố cáo còn phải ghi rõ họ tên, địa chỉ, cách thức liên hệ với từng người tố cáo; họ tên của người đại diện cho những người tố cáo. Người tố cáo phải ký tên hoặc điểm chỉ vào đơn tố cáo.",
                   "2) Trường hợp người tố cáo đến tố cáo trực tiếp tại thì người tiếp nhận hướng dẫn người tố cáo viết đơn tố cáo hoặc ghi lại nội dung tố cáo bằng văn bản và yêu cầu người tố cáo ký tên hoặc điểm chỉ xác nhận vào văn bản, trong đó ghi rõ nội dung theo quy định. Trường hợp nhiều người cùng tố cáo về cùng một nội dung thì người tiếp nhận hướng dẫn người tố cáo cử đại diện viết đơn tố cáo hoặc ghi lại nội dung tố cáo bằng văn bản và yêu cầu những người tố cáo ký tên hoặc điểm chỉ xác nhận vào văn bản.",
                   "Trong thời hạn 05 ngày làm việc kể từ ngày ra quyết định thụ lý tố cáo, người giải quyết tố cáo có trách nhiệm thông báo cho người tố cáo và thông báo về nội dung tố cáo cho người bị tố cáo biết."
                   ]
        link = [["Thông tin chi tiết",
                 "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=2.002396"]]

    elif intents == "khieu nai":
        bot_audio = "Chào bạn, sau đây là một số hướng dẫn thực hiện đơn khiếu nại tại Ủy ban nhân dân Xã/Phường"
        thu_tuc = ["I) Thực hiện khiều nại:",
                   "- Người khiếu nại trực tiếp hoặc nộp đơn khiếu nại trực tiếp tại bộ phận tiếp nhận và trả kết quả - UBND cấp xã hoặc gửi qua đường bưu điện. Nếu khiếu nại thuộc thẩm quyền giải quyết của chủ tịch UBND cấp xã theo quy định tại Điều 17 Luật khiếu nại, người khiếu nại phải gửi đơn và các tài liệu liên quan (nếu có)."]
        link = [["Thông tin chi tiết", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=2.002409"],
                ["Mẫu đơn khiếu nại",
                    "https://docs.google.com/document/d/15ss1yEHvJhHImA-nlRgdTDCurEzn0bn0/edit"],
                ["Mẫu giấy ủy quyền khiếu nại", "https://docs.google.com/document/d/1U7dihwJ1GlzQYsVwnCveIL02A0yev2De/edit"]]

    elif intents == "dang ky xe may":
        bot_audio = """Chào bạn, sau đây là một số hướng dẫn cho việc đăng ký, cấp biển số xe mô tô, xe gắn máy (kể cả xe máy điện) lần đầu tại Công an cấp xã"""
        thu_tuc = ["I) Giấy tờ cần chuẩn bị:",
                   "Giấy khai đăng ký xe (Mẫu số 01 ban hành kèm theo Thông tư số 58/2020/TT-BCA) (1 bản chính và 1 bản sao)",
                   "Giấy tờ chuyển quyền sở hữu xe. (1 bản chính và 1 bản sao)",
                   "Giấy tờ lệ phí trước bạ. (1 bản chính và 1 bản sao)",
                   "Giấy tờ nguồn gốc xe. (1 bản chính và 1 bản sao)",
                   "Giấy tờ của chủ xe. (1 bản chính và 1 bản sao)",
                   "II) Cách thức thực hiện có 2 hình thức trực tiếp và trực tuyến.",
                   "1) Trực tiếp: là đến tại trụ sở Công an cấp xã được phân cấp công tác đăng ký xe. Thời gian: Từ thứ 2 đến thứ 7 (theo quy định của Thủ tướng Chính phủ). Cấp ngay biển số sau khi tiếp nhận hồ sơ đăng ký xe hợp lệ; cấp giấy chứng nhận đăng ký xe thì thời hạn hoàn thành thủ tục không quá 2 ngày làm việc, kể từ ngày nhận hồ sơ hợp lệ.",
                   "2) Trực tuyến: là nộp Giấy khai đăng ký xe trên Cổng Dịch vụ công quốc gia hoặc Cổng dịch vụ công Bộ Công an. Cấp ngay biển số sau khi tiếp nhận hồ sơ đăng ký xe hợp lệ; cấp giấy chứng nhận đăng ký xe thì thời hạn hoàn thành thủ tục không quá 2 ngày làm việc, kể từ ngày nhận hồ sơ hợp lệ.",
                   "III) Lệ phí đăng ký xe máy:",
                   "- Tại Hà Nội và TP. Hồ Chí Minh:",
                   "+ Xe có giá trị từ 15 triệu đồng trở xuống: Lệ phí từ 500.000 đồng - 01 triệu đồng",
                   "+ Xe có giá trị từ 15 triệu đồng đến 40 triệu đồng: Từ 01 triệu - 02 triệu đồng",
                   "+ Xe có giá trị trên 40 triệu đồng: Từ 02 triệu đồng - 04 triệu đồng",
                   "- Đối với các thành phố trực thuộc trung ương khác, các thành phố trực thuộc tỉnh và các thị xã:",
                   "+ Xe có giá trị từ 15 triệu đồng trở xuống: 200.000 đồng",
                   "+ Xe có giá trị từ 15 triệu đồng - 40 triệu đồng: 400.000 đồng",
                   "+ Xe có giá trị từ trên 40 triệu đồng: 800.000 đồng",
                   "- Đối với các địa phương khác thì 50.000 đồng đối với tất cả các loại xe."
                   ]
        link = [["Thông tin thêm", "https://dichvucong.gov.vn/p/home/dvc-tthc-thu-tuc-hanh-chinh-chi-tiet.html?ma_thu_tuc=299370&open_popup=1"],
                ["Mẫu số 1 Giấy khai đăng ký xe", "https://docs.google.com/document/d/1aeCwTsjIpXGGHPHPY7WxvvGVljBhTluk/edit"]]

    elif intents == "chao hoi":
        bot_audio = """Xin chào bạn, tôi là bot hỗ trợ giải đáp các thắc mắc tại Ủy ban hành chính xã phường, đừng ngần ngại việc hỏi, tôi sẽ giải đáp cho bạn"""
        thu_tuc = [""]
        link = [["Một số biểu mẫu hành chính", "bieumau"]]

    elif intents == "chuc nang":
        bot_audio = """Chức năng của tôi là hỗ trợ, giải đáp các thắc mắc của bạn về thủ tục hành chính tại Ủy ban 
        hành chính xã phường"""
        thu_tuc = [
            "Tôi có thể trả lời một số câu hỏi và bạn có thể tìm thấy các biểu mẫu hành chính ở tôi"]
        link = [["Một số biểu mẫu hành chính", "bieumau"]]

    elif intents == "make happy":
        bot_audio = """Tôi sẽ kể bạn nghe một chuyện.
        Vừa xong bữa nhậu đầu năm với bạn bè, anh chồng ngất ngư đi về nhà. Để vợ không đoán được là mình uống rượu quá mức, anh ta quyết định đi thẳng vào phòng và ngồi đọc sách, hy vọng vợ trông thấy sẽ nghĩ là mình tỉnh táo...Vài phút sau, cô vợ vào và hỏi:
        - Anh đang làm gì vậy?
        - Đọc sách.
        - Vợ anh ta thét lên: Đồ điên! Đóng vali lại và ngủ đi!"""
        thu_tuc = [""]
        link = [["", ""]]

    elif intents == "tam biet":
        bot_audio = "Tạm biệt bạn, chúc bạn một ngày vui vẻ."
        thu_tuc = [""]
        link = [["", ""]]

    elif intents == "tam trang buon":
        bot_audio = "Buồn làm chi em ơi, lá xanh rồi cũng phai màu"
        thu_tuc = [""]
        link = [["Một chút không khí vui vẻ", "https://www.youtube.com/watch?v=6depEZ1acKM"],
                ["Một chút âm nhạc", "https://www.youtube.com/watch?v=ahF-3SaeJJ4"]]

    elif intents == "chung thuc di chuc":
        bot_audio = "Xin chào bạn, sau đây là một số thủ tục cần thực hiện để chứng thực di chúc tại Ủy ban nhân dân Xã/Phường"
        thu_tuc = ["I) Hồ sơ yêu cầu chứng thực:",
                   "- Dự thảo di chúc. (1 bản chính)",
                   "- Bản sao Giấy chứng minh nhân dân/Căn cước công dân hoặc Hộ chiếu còn giá trị sử dụng của người yêu cầu chứng thực (1 bản sao, xuất trình kèm theo bản chính để đối chiếu)",
                   "- Bản sao giấy chứng nhận quyền sở hữu, quyền sử dụng hoặc bản sao giấy tờ thay thế được pháp luật quy định đối với tài sản mà pháp luật quy định phải đăng ký quyền sở hữu, quyền sử dụng trong trường hợp di chúc liên quan đến tài sản đó; trừ trường hợp người lập di chúc đang bị cái chết đe dọa đến tính mạng (1 bản sao, xuất trình kèm theo bản chính để đối chiếu).",
                   "II) Trình tự thực hiện",
                   "- Người yêu cầu chứng thực nộp 01 bộ hồ sơ yêu cầu chứng thực.",
                   "- Người thực hiện chứng thực (hoặc người tiếp nhận hồ sơ trong trường hợp tiếp nhận hồ sơ tại bộ phận một cửa, một cửa liên thông) kiểm tra giấy tờ trong hồ sơ yêu cầu chứng thực, nếu đầy đủ, tại thời điểm chứng thực người lập di chúc tự nguyện, minh mẫn và nhận thức, làm chủ được hành vi của mình thì thực hiện chứng thực.",
                   "- Người lập di chúc phải ký trước mặt người thực hiện chứng thực, nếu di chúc có từ hai trang trở lên thì phải ký vào từng trang. Trường hợp người yêu cầu chứng thực nộp hồ sơ tại bộ phận một cửa, một cửa liên thông thì phải ký trước mặt người tiếp nhận hồ sơ.",
                   "- Trường hợp người yêu cầu chứng thực không ký được thì phải điểm chỉ; nếu người đó không đọc được, không nghe được, không ký, không điểm chỉ được thì phải có 02 (hai) người làm chứng. Người làm chứng phải có đủ năng lực hành vi dân sự và không có quyền, lợi ích hoặc nghĩa vụ liên quan đến giao dịch. Người làm chứng do người yêu cầu chứng thực bố trí. Trường hợp người yêu cầu chứng thực không bố trí được thì đề nghị cơ quan thực hiện chứng thực chỉ định người làm chứng",
                   "- Người thực hiện chứng thực (hoặc người tiếp nhận hồ sơ) ghi lời chứng theo mẫu quy định. Trường hợp tiếp nhận hồ sơ tại bộ phận một cửa, một cửa liên thông thì người tiếp nhận hồ sơ ký vào từng trang của di chúc và ký vào dưới lời chứng theo mẫu quy định.",
                   " Người thực hiện chưng thực ký vào từng trang của di chúc (nếu hồ sơ không được tiếp nhận qua bộ phận một cửa, một chửa liên thông), ký, ghi rõ họ tên, đóng dấu của cơ quan thực hiện chứng thực và ghi vào sổ chứng thực.",
                   " Đối với di chúc có từ 02 (hai) trang trở lên, thì từng trang phải được đánh số thứ tự, có chữ ký của người yêu cầu chứng thực và người thực hiện chứng thực; số lượng trang và lời chứng được ghi tại trang cuối của di chúc. Trường hợp di chúc có từ 02 (hai) tờ trở lên thì phải đóng dấu giáp lai."]
        link = [["Thông tin tham khảo", "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=2.001019"],
                ["Di chúc chưa được chứng thực có hợp lệ hay không", "https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/thoi-su-phap-luat/tu-van-phap-luat/23859/khi-nao-di-chuc-khong-cong-chung-chung-thuc-duoc-xem-la-hop-phap"]]

    elif intents == "di chuc chua chung thuc":
        bot_audio = "Pháp luật không quy định di chúc bắt buộc phải được công chứng, mà có thể được lập dưới nhiều hình thức khác nhau như di chúc bằng văn bản không có người làm chứng, có người làm chứng, có công chứng hoặc chứng thực. Ngoài ra, còn có thể lập di chúc bằng miệng."
        thu_tuc = ["I) Di chúc được lập bằng văn bản mà không có công chứng, chứng thực thì chỉ được coi là hợp pháp nếu đáp ứng đủ các điều kiện sau:",
                   "- Người lập di chúc minh mẫn, sáng suốt trong khi lập di chúc; không bị lừa dối, đe doạ, cưỡng ép;",
                   "- Nội dung của di chúc không vi phạm điều cấm của luật, không trái đạo đức xã hội; hình thức di chúc không trái quy định của luật.",
                   "II) Điều 630 của Bộ luật dân sự 2015 quy định di chúc hợp pháp:",
                   "1. Di chúc hợp pháp phải có đủ các điều kiện sau đây:",
                   "a) Người lập di chúc minh mẫn, sáng suốt trong khi lập di chúc; không bị lừa dối, đe doạ, cưỡng ép;",
                   "b) Nội dung của di chúc không vi phạm điều cấm của luật, không trái đạo đức xã hội; hình thức di chúc không trái quy định của luật."
                   "2. Di chúc của người từ đủ mười lăm tuổi đến chưa đủ mười tám tuổi phải được lập thành văn bản và phải được cha, mẹ hoặc người giám hộ đồng ý về việc lập di chúc.",
                   "3. Di chúc của người bị hạn chế về thể chất hoặc của người không biết chữ phải được người làm chứng lập thành văn bản và có công chứng hoặc chứng thực.",
                   "4. Di chúc bằng văn bản không có công chứng, chứng thực chỉ được coi là hợp pháp, nếu có đủ các điều kiện được quy định tại khoản 1 Điều này.",
                   "5. Di chúc miệng được coi là hợp pháp nếu người di chúc miệng thể hiện ý chí cuối cùng của mình trước mặt ít nhất hai người làm chứng và ngay sau khi người di chúc miệng thể hiện ý chí cuối cùng, người làm chứng ghi chép lại, cùng ký tên hoặc điểm chỉ. Trong thời hạn 05 ngày làm việc, kể từ ngày người di chúc miệng thể hiện ý chí cuối cùng thì di chúc phải được công chứng viên hoặc cơ quan có thẩm quyền chứng thực xác nhận chữ ký hoặc điểm chỉ của người làm chứng.",
                   ]
        link = [["Hướng dẫn chứng thực di chúc",
                 "https://dichvucong.gov.vn/p/home/dvc-chi-tiet-thu-tuc-hanh-chinh.html?ma_thu_tuc=2.001019"]]

    elif intents == "cong chung":
        bot_audio = "Chào bạn, dưới đây là một số hướng dẫn khi thực hiện công chứng tại Ủy ban nhân dân xã/phường"
        thu_tuc = ["I) Trình tự thực hiện:",
                   "1) Nộp hồ sơ tại “Bộ phận tiếp nhận và trả kết quả” của UBND xã, phường, thị trấn (UBND cấp xã) vào giờ hành chính các ngày làm việc trong tuần (trừ ngày nghỉ, ngày nghỉ lễ theo quy định).",
                   "2) Công chức tiếp nhận hồ sơ, kiểm tra tính pháp lý và nội dung hồ sơ:",
                   "- Nếu hồ sơ hợp lệ thì người nộp hồ sơ sẽ được nhận phiếu biên nhận",
                   "- Nếu hồ sơ chưa hợp lệ thì sẽ có người hướng dẫn để hoàn thiện hồ sơ",
                   "3) Nộp lệ phí theo tùy theo loại giấy tờ và số lượng giấy tờ thực hiện chứng thực.",
                   "4) Dựa theo thông tin phiếu biên nhận để nhận kết quả tại “Bộ phận tiếp nhận và trả kết quả” của UBND cấp xã",
                   "II) Có 8 trường hợp chứng thực giấy tờ có thể thực hiện tại UBND xã, phường:",
                   "(1) Chứng thực bản sao từ bản chính các giấy tờ, văn bản do cơ quan có thẩm quyền của Việt Nam cấp hoặc chứng nhận;",
                   "(2) Chứng thực chữ ký trong các giấy tờ, văn bản, trừ việc chứng thực chữ ký người dịch;",
                   "(3) Chứng thực hợp đồng, giao dịch liên quan đến tài sản là động sản;",
                   "(4) Chứng thực hợp đồng, giao dịch liên quan đến thực hiện các quyền của người sử dụng đất theo quy định của Luật Đất đai;",
                   "(5) Chứng thực hợp đồng, giao dịch về nhà ở theo quy định của Luật Nhà ở;",
                   "(6) Chứng thực di chúc;",
                   "(7) Chứng thực văn bản từ chối nhận di sản;",
                   "(8) Chứng thực văn bản thỏa thuận phân chia di sản, văn bản khai nhận di sản mà di sản là động sản, quyền sử dụng đất hoặc nhà ở."
                   ]
        link = [["Nghị định số 23/2015/NĐ-CP của Chính phủ: Về cấp bản sao từ sổ gốc, chứng thực bản sao từ bản chính, chứng thực chữ ký và chứng thực hợp đồng, giao dịch",
                 "https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=179100"]]

    elif intents == "chung thuc":
        bot_audio = "Chào bạn, dưới đây là một số hướng dẫn khi thực hiện chứng thực tại Ủy ban nhân dân xã/phường"
        thu_tuc = ["I) Trình tự thực hiện:",
                   "1) Nộp hồ sơ tại “Bộ phận tiếp nhận và trả kết quả” của UBND xã, phường, thị trấn (UBND cấp xã) vào giờ hành chính các ngày làm việc trong tuần (trừ ngày nghỉ, ngày nghỉ lễ theo quy định).",
                   "2) Công chức tiếp nhận hồ sơ, kiểm tra tính pháp lý và nội dung hồ sơ:",
                   "- Nếu hồ sơ hợp lệ thì người nộp hồ sơ sẽ được nhận phiếu biên nhận",
                   "- Nếu hồ sơ chưa hợp lệ thì sẽ có người hướng dẫn để hoàn thiện hồ sơ",
                   "3) Nộp lệ phí theo tùy theo loại giấy tờ và số lượng giấy tờ thực hiện chứng thực.",
                   "4) Dựa theo thông tin phiếu biên nhận để nhận kết quả tại “Bộ phận tiếp nhận và trả kết quả” của UBND cấp xã",
                   "II) Có 8 trường hợp chứng thực giấy tờ có thể thực hiện tại UBND xã, phường:",
                   "(1) Chứng thực bản sao từ bản chính các giấy tờ, văn bản do cơ quan có thẩm quyền của Việt Nam cấp hoặc chứng nhận;",
                   "(2) Chứng thực chữ ký trong các giấy tờ, văn bản, trừ việc chứng thực chữ ký người dịch;",
                   "(3) Chứng thực hợp đồng, giao dịch liên quan đến tài sản là động sản;",
                   "(4) Chứng thực hợp đồng, giao dịch liên quan đến thực hiện các quyền của người sử dụng đất theo quy định của Luật Đất đai;",
                   "(5) Chứng thực hợp đồng, giao dịch về nhà ở theo quy định của Luật Nhà ở;",
                   "(6) Chứng thực di chúc;",
                   "(7) Chứng thực văn bản từ chối nhận di sản;",
                   "(8) Chứng thực văn bản thỏa thuận phân chia di sản, văn bản khai nhận di sản mà di sản là động sản, quyền sử dụng đất hoặc nhà ở."
                   ]
        link = [["Nghị định số 23/2015/NĐ-CP của Chính phủ: Về cấp bản sao từ sổ gốc, chứng thực bản sao từ bản chính, chứng thực chữ ký và chứng thực hợp đồng, giao dịch",
                 "https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=179100"]]

    elif intents == "cong chung khong co ban goc":
        bot_audio = "Theo như Nghị định số 23/2015/NĐ-CP của Chính phủ thì khi thực hiện chứng thực tài liệu bất kì, bắt buộc phải xuất trình bản chính để làm cơ sở chứng minh."
        thu_tuc = ["- Theo như quy định: ",
                   "Bản sao là bản chụp từ bản chính hoặc bản đánh máy có nội dung đầy đủ, chính xác như nội dung ghi trong sổ gốc.",
                   "- Như đã nói ở trên, việc chứng thực mà không xuất trình được bản gốc là không hợp lệ, tuy nhiên hiện nay vẫn có một số loại giấy tờ được phép chứng thực mặc dù không xuất trình được bản chính nếu có thể chứng minh qua hình ảnh, hoặc giấy tờ khác có liên quan."]
        link = [["Nghị định số 23/2015/NĐ-CP của Chính phủ: Về cấp bản sao từ sổ gốc, chứng thực bản sao từ bản chính, chứng thực chữ ký và chứng thực hợp đồng, giao dịch",
                 "https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=179100"]]

    return bot_audio, thu_tuc, link

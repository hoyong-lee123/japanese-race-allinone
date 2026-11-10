"""
일본 중앙경마(JRA) 연간 전체 G1 레이스 캘린더 및 역사적 명승부
"""

G1_RACES = [
    {
        "name": "페브러리 스테이크스 (February Stakes)",
        "jp_name": "フェブラリーステークス",
        "month": "2월 중순",
        "racetrack": "도쿄 경마장",
        "surface": "더트 (Dirt) 1,600m",
        "eligibility": "4세 이상 (오픈)",
        "first_prize": "1억 2,000만 엔",
        "description": "JRA 한 해의 시작을 알리는 첫 번째 G1 경주. 일본 더트 마일 챔피언 결정전.",
        "recent_winner": "페페 드 시에로 / 레몬 팝"
    },
    {
        "name": "타카마츠노미야 기념 (Takamatsunomiya Kinen)",
        "jp_name": "高松宮記念",
        "month": "3월 하순",
        "racetrack": "주쿄 경마장",
        "surface": "잔디 (Turf) 1,200m",
        "eligibility": "4세 이상 (오픈)",
        "first_prize": "1억 7,000만 엔",
        "description": "봄철 단거리 최강마를 가리는 스프린트 G1. 주쿄의 가파른 언덕이 승부처.",
        "recent_winner": "매드 쿨"
    },
    {
        "name": "오사카배 (Osaka Hai)",
        "jp_name": "大阪杯",
        "month": "3월 말 ~ 4월 초",
        "racetrack": "한신 경마장",
        "surface": "잔디 (Turf) 2,000m",
        "eligibility": "4세 이상 (오픈)",
        "first_prize": "2억 엔",
        "description": "봄철 고마(4세 이상) 중거리 왕도 제1탄. 한신의 내선 코스 2000m에서 격돌.",
        "recent_winner": "베라 아즈르 / 베르트라이젠데"
    },
    {
        "name": "오카상 (Cherry Blossom Sho / Japanese 1000 Guineas)",
        "jp_name": "桜花賞",
        "month": "4월 초순",
        "racetrack": "한신 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "3세 암말 (牝馬)",
        "first_prize": "1억 4,000만 엔",
        "description": "암말 클래식 삼관(트리플 티아라) 제1탄. '가장 빠른 암말이 이긴다.'",
        "recent_winner": "스텔라 벨로체 / 리버티 아일랜드 / 스텔렌보쉬"
    },
    {
        "name": "사츠키상 (Japanese 2000 Guineas)",
        "jp_name": "皐月賞",
        "month": "4월 중순",
        "racetrack": "나카야마 경마장",
        "surface": "잔디 (Turf) 2,000m",
        "eligibility": "3세 암/수 (클래식)",
        "first_prize": "2억 엔",
        "description": "클래식 삼관 제1탄. 나카야마 2000m의 급경사를 넘어서 '가장 빠른 말이 이긴다.'",
        "recent_winner": "저스틴 밀라노 / 솔 오리엔스 / 지오글리프"
    },
    {
        "name": "텐노상 (봄) (Tenno Sho Spring)",
        "jp_name": "天皇賞（春）",
        "month": "4월 말 ~ 5월 초",
        "racetrack": "교토 경마장",
        "surface": "잔디 (Turf) 3,200m",
        "eligibility": "4세 이상 (오픈)",
        "first_prize": "2억 2,000만 엔",
        "description": "전통과 권위의 천황상. JRA 평지 최장거리 G1으로 스태미너의 극한을 시험.",
        "recent_winner": "테오 로얄 / 저스틴 팰리스 / 타이틀홀더"
    },
    {
        "name": "NHK 마일 컵 (NHK Mile Cup)",
        "jp_name": "NHKマイルカップ",
        "month": "5월 초순",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "3세 암/수 (오픈)",
        "first_prize": "1억 3,000만 엔",
        "description": "3세 마일 왕을 결정하는 무대. 단거리/마일 적성의 3세마들이 총집결.",
        "recent_winner": "샴페인 컬러 / 장 탈루"
    },
    {
        "name": "빅토리아 마일 (Victoria Mile)",
        "jp_name": "ヴィクトリアマイル",
        "month": "5월 중순",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "4세 이상 암말 (牝馬)",
        "first_prize": "1억 3,000만 엔",
        "description": "고마 암말들의 봄철 마일 정점 대결. 아몬드 아이, 그란 알레그리아, 소다시 우승.",
        "recent_winner": "텐 해피 로즈 / 송라인 / 소다시"
    },
    {
        "name": "우준 빈마 / 오크스 (Japanese Oaks)",
        "jp_name": "優駿牝馬（オークス）",
        "month": "5월 하순",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 2,400m",
        "eligibility": "3세 암말 (牝馬)",
        "first_prize": "1억 5,000만 엔",
        "description": "암말 클래식 제2탄. 1600m에서 단숨에 2400m로 늘어난 거리를 극복하는 여왕 선발전.",
        "recent_winner": "체르비니아 / 리버티 아일랜드 / 스타즈 온 어스"
    },
    {
        "name": "도쿄 유슌 / 일본 더비 (Tokyo Yushun / Japanese Derby)",
        "jp_name": "東京優駿（日本ダービー）",
        "month": "5월 말 ~ 6월 초",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 2,400m",
        "eligibility": "3세 암/수 (클래식)",
        "first_prize": "3억 엔",
        "description": "모든 경마인의 필생의 꿈. 8,000여 두의 동기생 중 단 한 마리만이 차지하는 최고의 영광. '가장 운이 좋은 말이 이긴다.'",
        "recent_winner": "다논 데사이 / 타스티에라 / 도듀스 / 샤흐리야르"
    },
    {
        "name": "야스다 기념 (Yasuda Kinen)",
        "jp_name": "安田記念",
        "month": "6월 초순",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "3세 이상 (오픈)",
        "first_prize": "1억 8,000만 엔",
        "description": "봄철 마일의 총결산. 해외 원정마도 다수 참전하는 아시아 최고 수준의 마일 레이스.",
        "recent_winner": "로맨틱 워리어 (홍콩) / 송라인"
    },
    {
        "name": "타카라즈카 기념 (Takarazuka Kinen)",
        "jp_name": "宝塚記念",
        "month": "6월 하순",
        "racetrack": "한신 경마장",
        "surface": "잔디 (Turf) 2,200m",
        "eligibility": "3세 이상 (오픈 팬투표)",
        "first_prize": "2억 2,000만 엔",
        "description": "상반기 그랑프리. 팬 투표로 출전마를 선발하며, 장마철 거친 마장과 치열한 몸싸움이 특징.",
        "recent_winner": "블로우 더 혼 / 이퀴녹스 / 타이틀홀더"
    },
    {
        "name": "스프린터즈 스테이크스 (Sprinters Stakes)",
        "jp_name": "スプリンターズステークス",
        "month": "9월 말 ~ 10월 초",
        "racetrack": "나카야마 경마장",
        "surface": "잔디 (Turf) 1,200m",
        "eligibility": "3세 이상 (오픈)",
        "first_prize": "1억 7,000만 엔",
        "description": "가을 단거리 제왕전. 나카야마의 짧은 직선에서 눈 깜짝할 사이에 끝나는 초광속 승부.",
        "recent_winner": "루갈 / 마마 코차 / 잭 도르"
    },
    {
        "name": "슈카상 (Shuka Sho)",
        "jp_name": "秋華賞",
        "month": "10월 중순",
        "racetrack": "교토 경마장",
        "surface": "잔디 (Turf) 2,000m",
        "eligibility": "3세 암말 (트리플 티아라 최종전)",
        "first_prize": "1억 1,000만 엔",
        "description": "암말 삼관의 마지막 관문. 교토 내선 코스의 좁은 코너를 도는 박진감 넘치는 승부.",
        "recent_winner": "체르비니아 / 리버티 아일랜드 (삼관 달성)"
    },
    {
        "name": "킷카상 (Kikuka Sho / Japanese St. Leger)",
        "jp_name": "菊花賞",
        "month": "10월 하순",
        "racetrack": "교토 경마장",
        "surface": "잔디 (Turf) 3,000m",
        "eligibility": "3세 암/수 (클래식 최종전)",
        "first_prize": "2억 엔",
        "description": "클래식 삼관의 마지막 관문. 요도의 언덕을 두 번 넘는 극한의 3000m. '가장 강한 말이 이긴다.'",
        "recent_winner": "어반 시크 / 두레차 / 아스커 빅터 모어"
    },
    {
        "name": "텐노상 (가을) (Tenno Sho Autumn)",
        "jp_name": "天皇賞（秋）",
        "month": "10월 말",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 2,000m",
        "eligibility": "3세 이상 (오픈)",
        "first_prize": "2억 2,000만 엔",
        "description": "가을 중거리 절대 최강마 결정전. 역대급 스피드와 명승부(이퀴녹스 1:55.2 세계기록) 배출.",
        "recent_winner": "도듀스 (2024) / 이퀴녹스 (2022, 2023)"
    },
    {
        "name": "엘리자베스 여왕배 (Queen Elizabeth II Cup)",
        "jp_name": "エリザベス女王杯",
        "month": "11월 중순",
        "racetrack": "교토 경마장",
        "surface": "잔디 (Turf) 2,200m",
        "eligibility": "3세 이상 암말 (牝馬)",
        "first_prize": "1억 3,000만 엔",
        "description": "3세 암말과 고마 암말이 세대를 뛰어넘어 중장거리 최강 여왕을 가리는 무대.",
        "recent_winner": "스터닝 로즈 / 제럴디나 / 아카이토리노 무스메"
    },
    {
        "name": "마일 챔피언십 (Mile Championship)",
        "jp_name": "マイルチャンピオンシップ",
        "month": "11월 하순",
        "racetrack": "교토 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "3세 이상 (오픈)",
        "first_prize": "1억 8,000만 엔",
        "description": "가을 마일의 최고봉. 교토 외선 코스에서 펼쳐지는 극한의 스피드 스퍼트.",
        "recent_winner": "나뮬 / 세리포스 / 그란 알레그리아"
    },
    {
        "name": "재팬 컵 (Japan Cup)",
        "jp_name": "ジャパンカップ",
        "month": "11월 말",
        "racetrack": "도쿄 경마장",
        "surface": "잔디 (Turf) 2,400m",
        "eligibility": "3세 이상 (국제 초대 오픈)",
        "first_prize": "5억 엔 (JRA 최고 상금)",
        "description": "세계 각국의 톱 클래스 명마들이 도쿄 2400m에서 격돌하는 세계 최고 권위의 국제 경주.",
        "recent_winner": "이퀴녹스 (2023) / 벨라 아즈르 (2022) / 콘트레일 (2021)"
    },
    {
        "name": "챔피언스 컵 (Champions Cup)",
        "jp_name": "チャンピオンズカップ",
        "month": "12월 초순",
        "racetrack": "주쿄 경마장",
        "surface": "더트 (Dirt) 1,800m",
        "eligibility": "3세 이상 (더트)",
        "first_prize": "1억 2,000만 엔",
        "description": "하반기 더트 챔피언 결정전. 모래밭 위의 최강자를 가리는 숨 막히는 파워 레이스.",
        "recent_winner": "레몬 팝 / 준 라이트 볼트 / 테오 케인즈"
    },
    {
        "name": "한신 쥬브나일 필리즈 (Hanshin Juvenile Fillies)",
        "jp_name": "阪神ジュベナイルフィリーズ",
        "month": "12월 중순",
        "racetrack": "한신 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "2세 암말 한정",
        "first_prize": "6,500만 엔",
        "description": "2세 여왕 결정전. 이듬해 클래식 전선의 유력 후보를 점치는 바로미터.",
        "recent_winner": "아스콜리 피체노 / 리버티 아일랜드 / 소다시"
    },
    {
        "name": "아사히배 퓨처리티 스테이크스 (Asahi Hai Futurity Stakes)",
        "jp_name": "朝日杯フューチュリティステークス",
        "month": "12월 중순",
        "racetrack": "한신 경마장",
        "surface": "잔디 (Turf) 1,600m",
        "eligibility": "2세 수/암말",
        "first_prize": "7,000만 엔",
        "description": "2세 마일 챔피언 결정전. 미래의 스타 명마들이 첫 G1 트로피를 두고 다투는 무대.",
        "recent_winner": "점보 카펠라 / 도루체 모어 / 도듀스"
    },
    {
        "name": "아리마 기념 (Arima Kinen / The Grand Prix)",
        "jp_name": "有馬記念",
        "month": "12월 마지막 일요일",
        "racetrack": "나카야마 경마장",
        "surface": "잔디 (Turf) 2,500m",
        "eligibility": "3세 이상 (팬투표 선발)",
        "first_prize": "5억 엔 (재팬컵과 공동 1위)",
        "description": "일본 한 해를 마무리하는 최대의 국민적 스포츠 축제. 단일 레이스 마권 매출 세계 1위 기록.",
        "recent_winner": "도듀스 (2023) / 이퀴녹스 (2022) / 에프포리아 (2021)"
    },
    {
        "name": "호프풀 스테이크스 (Hopeful Stakes)",
        "jp_name": "ホープフルステークス",
        "month": "12월 28일경",
        "racetrack": "나카야마 경마장",
        "surface": "잔디 (Turf) 2,000m",
        "eligibility": "2세 수/암말",
        "first_prize": "7,000만 엔",
        "description": "이듬해 사츠키상과 동일한 코스에서 열리는 2세 중거리 챔피언 결정전. 한 해 중앙경마의 최종전.",
        "recent_winner": "레갈레이라 (암말 우승) / 두라에레데 / 콘트레일"
    }
]


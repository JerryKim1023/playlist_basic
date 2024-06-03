// 오늘 그만보기 기능 구현
const todayButton = document.getElementById('today-button');
const closeButton = document.getElementById('close-button');
const popup = document.getElementById('today-popup');

// 팝업 닫기
closeButton.addEventListener('click', () => {
  popup.style.display = 'none';
});

// 오늘 그만보기 버튼 클릭 시 팝업 닫기 및 저장
todayButton.addEventListener('click', () => {
  popup.style.display = 'none';
  localStorage.setItem('today-visited', true);
});

// 로컬 스토리지에 저장된 값에 따라 팝업 표시 여부 결정
if (localStorage.getItem('today-visited')) {
  popup.style.display = 'none';
} else {
  popup.style.display = 'block';
}
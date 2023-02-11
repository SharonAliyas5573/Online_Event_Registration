function startTimer(targetDate) {
    const days = document.getElementById("days");
    const hours = document.getElementById("hours");
    const minutes = document.getElementById("mins");
    const seconds = document.getElementById("secs");
  
    function updateTimer() {
      const currentDate = new Date();
      const timeLeft = targetDate - currentDate;
  
      if (timeLeft < 0) {
        clearInterval(timer);
        return;
      }
  
      const daysLeft = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
      const hoursLeft = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutesLeft = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
      const secondsLeft = Math.floor((timeLeft % (1000 * 60)) / 1000);
  
      days.innerHTML = addLeadingZeros(daysLeft);
      hours.innerHTML = addLeadingZeros(hoursLeft);
      minutes.innerHTML = addLeadingZeros(minutesLeft);
      seconds.innerHTML = addLeadingZeros(secondsLeft);
    }
  
    function addLeadingZeros(value) {
      return value < 10 ? `0${value}` : value;
    }
  
    updateTimer();
    const timer = setInterval(updateTimer, 1000);
  }
  
  const targetDate = new Date("2023-03-11T05:59:59");
  startTimer(targetDate);
  
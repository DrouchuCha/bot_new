const tg = window.Telegram?.WebApp;
if (tg) {
  tg.expand();
  const user = tg.initDataUnsafe?.user;
  document.getElementById("user").innerText =
    user ? `👤 ${user.first_name} (${user.id})` : "Открыто вне Telegram";
}

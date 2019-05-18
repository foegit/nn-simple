async function predict(data, predict_for) {
  const data_json = JSON.stringify({
    data,
    predict: predict_for
  });

  const reqOptions = {
    method: 'post',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: data_json,
  }

  const res = await fetch('/predict', reqOptions);
  const val = await res.json();
  console.log(val)
  if (val.error) {
    const errOut = document.getElementById('data-error');
    errOut.innerText = val.error;
    return '';
  } else {
    return val.val;
  }

}

function handleData() {
  const errorOut = document.getElementById('data-error');
  const data = document.getElementById('data');
  const err = false;

  if (data.value.length == 0) {
    err = 'Empty string'
  }

  if (err) {
    errorOut.innerText = err;
    return false;
  }

  return true;
}

window.addEventListener('load', () => {
  const data = document.getElementById('data');
  const predictVal = document.getElementById('predict-val');
  const predictBtn = document.getElementById('predict-btn');
  const predictOut = document.getElementById('predicted-val');
  console.log(predictOut);

  data.addEventListener('input', () => {
    document.getElementById('data-error').innerText = '';
    handleData();
  });

  predictBtn.addEventListener('click', async (e) => {
    e.preventDefault();
    console.log(predictOut, '<<<');
    predictOut.value = await predict(data.value, predictVal.value);
  });
});

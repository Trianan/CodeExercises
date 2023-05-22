<?php
  $title = "#4: Largest palindrome product";
  $author = "Trianan";
  $question = "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.";
  $plan = "";
  $verified_answer = 906609;
?>

<!DOCTYPE html>
<html>

  <head>
    <title><?= $title ?></title>
    <link href="./resources/styles/style.css" type="text/css" rel="stylesheet">
  </head>

  <body>
    <header>
      <h1>Project Euler: PHP-Edition</h1>
      <h2><?= $title ?><br>By: <?= $author ?></h1>
      <nav><a href="./index.php">Home</a></nav>
    </header>

    <div id="output">
      <p>
        PROGRAM OUTPUT:
      </p>
      <code>
        <?php
          echo '-> call your function here <-';
        ?>
      </code>
      <p>
        CALCULATED ANSWER:
        <?= 'calculated answer here' ?>
      </p>
    </div>

    <div id="problem-sheet">
      <div id="question">
        <h2>Question:</h2>
        <p>
          <?= $question ?>
        </p>
      </div>
      <div id="plan">
        <h2>Plan:</h2>
        <p>
          <?= $plan ?>
        </p>
      </div>

      <div id="answer">
        <h2>Answer:</h2>
        <p>Verified: <?= $verified_answer ?></p>
        <p>Calculated: <?= 'calculated answer here' ?>
        <?php
          if ('calculated answer here' == $verified_answer) {
            echo "<p class='green'>✓</p>";
          }
          else {
            echo "<p class='red'>✕</p>";
          }
        ?>
      </div>
    </div>

    <footer>
      <div id="footer-links">
        <div>
          <a href="./problem_3.php">&lt-- PREVIOUS</a>
          <a href="./problem_5.php">NEXT --&gt</a>
        </div>
        <a href="./index.php">* HOME *</a>
      </div>
    </footer>
  </body>

</html>
# Nature-inspired Metaheuristic: Fireflies

Implementation of nature-inspired search algorithm:
- Firefly Algorithm [[Yang, 2008](https://books.google.de/books?id=iVB_ETlh4ogC&lpg=PR5&ots=DwgyslGEp9&lr&hl=de&pg=PR5#v=onepage&q&f=false)]

## How to use the algorithm?

Double clicking on run.py will run the program directly. 

|parameter    | description                                                                        |domain          |
|:-----------:|------------------------------------------------------------------------------------|----------------|
|objective    | minimization or maximization problem                                               |'min' or 'max'  |
|dimensions   | dimensionality of solution-space                                                   |positive integer|
|poppulation  | size of the population, i.e. fireflies         |positive integer|
|min range    | lower bound of solution-space in all dimensions                                    |real number     |
|max range    | upper bound of solution-space in all dimensions                                    |real number     |
|iterations   | number of iterations                                                               |positive integer|

### The Firefly Algorithm

|parameter    | description                                                                        |domain          |
|:-----------:|------------------------------------------------------------------------------------|----------------|
|alpha        | neighbor sphere radius                                                             |positive float  |
|beta         | maximum attractivneness                                                            |positive float  |
|gamma        | attractiveness descreasing factor                                                  |positive float  |

### The GUI is preloaded with some sample values
The more the number of iterations and size of population, the more time it'll take to display the output.
### How to get result:
On pressing the submit button, the computation begins. Once the computation is complete, then user will be able to see the resulting graph and the animated image of the optimization.
### What does clear button does?
Basically it will remove junk from the program folder.
While computing, the program generates number of images based on the number of iterations you have given. Once the images are generated those images are further converted into a single animated gif file. Which means that the image set which was generated earlier is of no use. Hence the clear button will clean up those images.

# Reference:
I took code for the fireflies algorithm from https://github.com/jonasgrebe/bees-bats-fireflies here.

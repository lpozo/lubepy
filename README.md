# Lubepy

**Lubepy** is a library that provides a set of basic calculations related to machinery lubrication. It's thought to be used by machinery lubrication technicians and engineers to quickly solve urgent lubrication problems on field.

## Installation

You might want to create a Python `virtualenv` before you install **Lubepy**. If so, you can run the following commands:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

Once you have the `virtualenv` in place and activated, you can install **Lubepy** as follows:

### On Linux systems:

```sh
(venv) $ pip install lubepy
```

## Usage Examples

Say you need to find the viscosity index of an oil. The oil has a viscosity at 40ºC of 104.7 cSt and a viscosity at 100ºC of 13.9 cSt. You can do something like this:

```python
from lubepy.lube.viscosity import viscosity_index
viscosity_index(104.7, 13.9)

# Output: 134
```

The viscosity index of an oil gives you an idea of how fast the viscosity diminishes when the temperature increases.

Now, suppose you have an oil with a viscosity index of 130 and a viscosity at 40ºC of 112 cSt. You need to know what will be the viscosity of your oil at 100ºC degrees. To solve this problem you can do something like this:

```python
from lubepy.lube.viscosity import viscosity_at_100
viscosity_at_100(112, 130)

# Output: 14.38
```

Most engines work at 100ºC, so it's important to know what will be the viscosity of an engine oil at 100ºC to have an idea of how well this oil will protect your engine.

There are a lot more calculations that you can perform with **Lubepy**. Unfortunately, they're not documented yet. If you want to get some additional information about the calculations implemented by **Lubepy**, then you can do something like this:

```python
>>> from lubepy.lube import viscosity
>>> help(viscosity)
```

    # Output
    Help on module lubepy.lube.viscosity in lubepy.lube:
    
    NAME
        lubepy.lube.viscosity - This module provides viscosity calculations.
    
    FUNCTIONS
        viscosity_at_100(viscosity40: float, index: float) -> float
            Calculate the Kinematic Viscosity (KV) at 100°C.
            
            Valid for viscosities between 2 and 500 cSt at 100°C.
        
        viscosity_at_40(viscosity100: float, index: float) -> float
    ...

## Authors

- Leodanis Pozo Ramos – Twitter: [@lpozo78](https://twitter.com/lpozo78) – E-mail: lpozor78@gmail.com
- Alexis Vega Jimenez: Provided formulas and theoretical support.

## Contribute to the Code

1. Make a fork (<https://github.com/lpozo/lubepy/fork>)
2. Clone your fork locally (`git clone https://github.com/your_user_name/lubepy.git`)
3. Create your feature branch (`git checkout -b feature_awesome_feature`)
4. Commit your changes (`git commit -am "Add some awesome feature"`)
5. Push to the branch (`git push -u origin feature_awesome_feature`)
6. Create a new Pull Request against the `develop` branch
7. Wait for code review and feedback

## License

Lubepy is distributed under the GNU General Pubic License, v2. See [LICENSE](https://github.com/lpozo/lubepy) for more information.

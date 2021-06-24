import styles from './styles.module.scss'

export function QSText(){

    return (
        <div className={styles.container}>
            <div className={styles.content}>
                <img src='/images/Aguia.svg' alt="Aguia" />
                <p>
                Constituída inteiramente por alunos do ITA e com sede no próprio instituto,
                a <span>CEE</span> surgiu em 2014 com a missão de trazer as melhores oportunidades para os alunos,
                promover o autoconhecimento e mostrar a eles como alcançar seus objetivos.
                </p>
            </div>
        </div>
    )
}
package com.unesc.myfinances.entities;

import java.math.BigDecimal;
import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.ForeignKey;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
@Table(name = "finances")
public class Finances {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "fin_id")
	private Long id;
	
	@ManyToOne
	@JoinColumn(name = "sit_id",  foreignKey = @ForeignKey(name = "fk_finances_situacao"))
	private Situacao situacao;
	
	@ManyToOne
	@JoinColumn(name = "fint_id",  foreignKey = @ForeignKey(name = "fk_finances_financesTipo"))
	private FinancesTipo financesTipo;
	
	@ManyToOne
	@JoinColumn(name = "usu_id",  foreignKey = @ForeignKey(name = "fk_finances_usuario"))
	private Usuario usuario;
	
	@Column(name = "fin_descricao", nullable = false, length = 240, unique = true)
	private String descricao;
	
	@Column(name = "fin_parcela", nullable = false, length = 30, unique = false)
	private Integer parcela;
	
	@Column(name = "fin_totalParcela", nullable = false, length = 30, unique = false)
	private Integer totalParcela;
	
	@Column(name = "fin_valorParcela", nullable = false, length = 30, unique = false)
	private BigDecimal valorParcela;
	
	@Column(name = "fin_valorTotal", nullable = false, length = 30, unique = false)
	private BigDecimal valorTotal;
	
	@Column(name = "fin_dataCadastro", nullable = false)
	private LocalDate dataCadastro;
	
	@Column(name = "fin_dataVencimento", nullable = false)
	private LocalDate dataVencimento;
}
